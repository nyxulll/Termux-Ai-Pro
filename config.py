import os
import json
from pathlib import Path

# Config directory: ~/.config/termux-ai-pro/
CONFIG_DIR = Path.home() / ".config" / "termux-ai-pro"
CONFIG_FILE = CONFIG_DIR / "config.json"

class Config:
    def __init__(self):
        self.data = {}
        self._load()

    def _load(self):
        """Loads config.json if it exists."""
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)

        if CONFIG_FILE.exists():
            try:
                with CONFIG_FILE.open("r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except Exception:
                # If the config is corrupted, reset it
                self.data = {}
        else:
            self.data = {}

    def save(self):
        """Saves config.json."""
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        with CONFIG_FILE.open("w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def get(self, key, default=None):
        """Gets a config value."""
        return self.data.get(key, default)

    def set(self, key, value):
        """Sets a config value and saves."""
        self.data[key] = value
        self.save()
