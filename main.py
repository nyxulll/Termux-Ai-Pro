#!/usr/bin/env python3
import sys
import os
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from config import Config
from providers.openai_provider import OpenAIProvider

console = Console()

APP_NAME = "Termux-AI-Pro"

PROVIDERS = {
    "openai": OpenAIProvider,
}

def choose_provider(cfg: Config):
    provider_name = cfg.get("provider", None)
    if provider_name and provider_name in PROVIDERS:
        return PROVIDERS[provider_name](cfg)
    console.print("Choose provider:")
    for i, name in enumerate(PROVIDERS.keys(), start=1):
        console.print(f"  {i}. {name}")
    choice = console.input("Provider number (1): ") or "1"
    try:
        idx = int(choice) - 1
        name = list(PROVIDERS.keys())[idx]
    except Exception:
        name = list(PROVIDERS.keys())[0]
    cfg.set("provider", name)
    return PROVIDERS[name](cfg)

def main():
    cfg = Config()
    cfg.ensure_dir()

    console.print(Panel(f"{APP_NAME}", title="Termux-AI-Pro"))

    provider = choose_provider(cfg)
    console.print("Type your message. Ctrl-C to exit.")

    try:
        while True:
            user_input = console.input("You> ")
            if user_input.strip() == "":
                continue
            try:
                console.print("Sending...")
                response = provider.send_message(user_input)
                console.print(Markdown(response))
            except Exception as e:
                console.print(f"Error: {e}")
    except KeyboardInterrupt:
        console.print("\nExiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()
