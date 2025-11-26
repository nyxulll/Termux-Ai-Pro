import os
import openai
from config import CONFIG_FILE

class OpenAIProvider:
    def __init__(self, cfg):
        self.cfg = cfg
        key = cfg.get("openai_api_key") or os.environ.get("OPENAI_API_KEY")
        if not key:
            from rich.console import Console
            console = Console()
            key = console.input("OpenAI API key: ")
            cfg.set("openai_api_key", key)
        openai.api_key = key

    def send_message(self, text: str) -> str:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}],
            max_tokens=512,
            temperature=0.7,
        )
        choices = resp.get("choices") or []
        if not choices:
            return "(no response)"
        return choices[0]["message"]["content"].strip()
