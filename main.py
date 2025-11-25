#!/usr/bin/env python3
import os
import sys
import json
import requests
import time
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from rich.live import Live
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, TextColumn

# --- Configuration & Paths ---
CONFIG_DIR = os.path.expanduser("~/.config/termux_ai_pro")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

DEFAULT_CONFIG = {
    "provider": "openrouter",
    "providers": {
        "openrouter": {
            "base_url": "https://openrouter.ai/api/v1",
            "api_key": "",
            "model": "deepseek/deepseek-r1:free",
            "name": "OpenRouter (Free)"
        },
        "gemini": {
            "base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
            "api_key": "",
            "model": "gemini-1.5-flash",
            "name": "Google Gemini"
        },
        "local": {
            "base_url": "http://127.0.0.1:11434/v1",
            "api_key": "termux",
            "model": "llama3",
            "name": "Local (Ollama)"
        },
        "custom": {
            "base_url": "https://api.openai.com/v1",
            "api_key": "",
            "model": "gpt-4o",
            "name": "Custom / OpenAI"
        }
    },
    "system_prompt": "You are a helpful AI assistant running in Termux CLI.",
    "stream": True
}

console = Console()

# --- Helpers ---
def load_config():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
    
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG
    
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            # Ensure new keys exist if updating from old version
            for k, v in DEFAULT_CONFIG.items():
                if k not in config:
                    config[k] = v
            return config
    except:
        return DEFAULT_CONFIG

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def print_banner():
    console.clear()
    banner = """
[bold cyan]╔════════════════════════════════════════╗[/]
[bold cyan]║   TERMUX AI PRO - UNIVERSAL CLIENT     ║[/]
[bold cyan]╚════════════════════════════════════════╝[/]
    """
    console.print(Align.center(banner))

# --- API Interaction ---
class AIClient:
    def __init__(self, config):
        self.config = config
        self.provider_key = config["provider"]
        self.settings = config["providers"][self.provider_key]
        self.history = []

    def stream_chat(self, user_input):
        messages = [{"role": "system", "content": self.config["system_prompt"]}] + self.history + [{"role": "user", "content": user_input}]
        
        headers = {
            "Authorization": f"Bearer {self.settings['api_key']}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://termux.com",
            "X-Title": "Termux AI Pro"
        }
        
        data = {
            "model": self.settings["model"],
            "messages": messages,
            "stream": True
        }
        
        # Determine URL (handle trailing slashes)
        base = self.settings['base_url'].rstrip('/')
        url = f"{base}/chat/completions"

        try:
            response = requests.post(url, headers=headers, json=data, stream=True, timeout=20)
            if response.status_code != 200:
                yield f"[bold red]Error {response.status_code}:[/] {response.text}"
                return

            full_msg = ""
            for line in response.iter_lines():
                if line:
                    decoded = line.decode('utf-8').replace('data: ', '')
                    if decoded == '[DONE]': break
                    try:
                        json_data = json.loads(decoded)
                        chunk = json_data['choices'][0]['delta'].get('content', '')
                        if chunk:
                            full_msg += chunk
                            yield chunk
                    except:
                        pass
            
            self.history.append({"role": "user", "content": user_input})
            self.history.append({"role": "assistant", "content": full_msg})

        except Exception as e:
            yield f"[bold red]Connection Error:[/] {str(e)}"

# --- Menus ---
def config_menu(config):
    while True:
        print_banner()
        curr = config["providers"][config["provider"]]
        console.print(Panel(f"""[bold]Current Provider:[/] {curr['name']}
[bold]Model:[/] {curr['model']}
[bold]API Key:[/] {curr['api_key'][:8]}...
[bold]Base URL:[/] {curr['base_url']}""", title="Settings"))

        console.print("[1] Switch Provider")
        console.print("[2] Edit Configuration")
        console.print("[3] Back")
        
        ch = Prompt.ask("Select", choices=["1", "2", "3"], default="3")
        
        if ch == "1":
            keys = list(config["providers"].keys())
            for i, k in enumerate(keys):
                console.print(f"[{i+1}] {config['providers'][k]['name']}")
            idx = int(Prompt.ask("Choice")) - 1
            if 0 <= idx < len(keys):
                config["provider"] = keys[idx]
                save_config(config)

        elif ch == "2":
            p = config["provider"]
            console.print(f"[yellow]Editing {p}... (Press Enter to keep current)[/]")
            
            new_key = Prompt.ask("API Key", default=config["providers"][p]["api_key"])
            new_model = Prompt.ask("Model Name", default=config["providers"][p]["model"])
            new_url = Prompt.ask("Base URL", default=config["providers"][p]["base_url"])
            
            config["providers"][p]["api_key"] = new_key
            config["providers"][p]["model"] = new_model
            config["providers"][p]["base_url"] = new_url
            save_config(config)

        elif ch == "3":
            break

def main():
    config = load_config()
    client = AIClient(config)
    
    # Check if first run (no API key for selected provider)
    if not config["providers"][config["provider"]]["api_key"] and "local" not in config["provider"]:
        console.print("[bold yellow]Welcome! It looks like you haven't set an API Key yet.[/]")
        if Prompt.ask("Go to settings now?", choices=["y", "n"]) == "y":
            config_menu(config)
            client = AIClient(config) # Reload client

    print_banner()
    console.print("[dim]Type 'exit' to quit, 'menu' for settings, 'clear' to reset chat.[/]")
    
    while True:
        try:
            prompt = Prompt.ask(f"\n[bold green]You[/]")
            
            if prompt.lower() in ['exit', 'quit']:
                console.print("[bold red]Goodbye![/]")
                break
            elif prompt.lower() == 'menu':
                config_menu(config)
                client = AIClient(config) # Reload client
                print_banner()
                continue
            elif prompt.lower() == 'clear':
                client.history = []
                console.clear()
                print_banner()
                continue
            
            # Chat Logic
            console.print(f"\n[bold cyan]{config['providers'][config['provider']]['name']}[/]")
            
            full_response = ""
            with Live(Markdown("..."), refresh_per_second=12) as live:
                for chunk in client.stream_chat(prompt):
                    full_response += chunk
                    live.update(Markdown(full_response))
            
        except KeyboardInterrupt:
            console.print("\n[bold red]Interrupted.[/]")
            break

if __name__ == "__main__":
    main()
