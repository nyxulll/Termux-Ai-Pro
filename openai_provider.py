import os
import openai
from config import Config

class OpenAIProvider:
    def __init__(self, cfg: Config):
        self.cfg = cfg

        # 1. Check environment variable first
        key = os.environ.get("OPENAI_API_KEY")

        # 2. If not found, check config file
        if not key:
            key = cfg.get("openai_api_key")

        # 3. If still not found, ask user with a friendly message
        if not key:
            from rich.console import Console
            console = Console()

            console.print("Welcome to Termux-AI-Pro!")
            key = console.input(
                "Please enter your OpenAI API key (you can paste it here)\n: "
            )

            # Save the key so user never has to enter it again
            cfg.set("openai_api_key", key)

        # 4. Set key for OpenAI usage
        openai.api_key = key

    def send_message(self, text: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}],
            max_tokens=500,
            temperature=0.7
        )

        return (
            response["choices"][0]["message"]["content"].strip()
            if response.get("choices")
            else "(no response)"
            )
            
