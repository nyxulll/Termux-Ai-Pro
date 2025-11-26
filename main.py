#!/usr/bin/env python3

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from config import Config
from providers.openai_provider import OpenAIProvider

console = Console()

APP_NAME = "Termux-AI-Pro"


def main():
    console.print(Panel(f"[bold cyan]{APP_NAME}[/bold cyan]", title="AI Terminal Client"))

    # Load config
    cfg = Config()

    # For now, only OpenAI provider is used
    provider = OpenAIProvider(cfg)

    console.print("[green]Type your message below. Press Ctrl + C to exit.[/green]\n")

    while True:
        try:
            user_input = console.input("[bold yellow]You:[/bold yellow] ").strip()
            if not user_input:
                continue

            console.print("[cyan]Thinking...[/cyan]")

            reply = provider.send_message(user_input)
            console.print(Markdown(reply))

        except KeyboardInterrupt:
            console.print("\n[red]Exiting... Goodbye![/red]")
            break

        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")


if __name__ == "__main__":
    main()
        
