import os
import json
from pathlib import Path

HOME = Path.home()
CONFIG_DIR = HOME / ".config" / "termux-ai-pro"
CONFIG_FILE = CONFIG_DIR / "config.json"

class Config:
    def __init__(self):
        self._data = {}
        self._loaded = False

    def ensure_dir(self):
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        if CONFIG_FILE.exists():
            try:
                with CONFIG_FILE.open("r", encoding="utf-8") as f:
                    self._data = json.load(f)
                    self._loaded = True
            except Exception:
                self._data = {}

    def save(self):
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        with CONFIG_FILE.open("w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=2)

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value
        self.save()
