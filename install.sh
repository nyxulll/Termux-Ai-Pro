#!/bin/bash
set -euo pipefail

echo "Termux-AI-Pro installer — started"

if ! command -v pkg >/dev/null 2>&1; then
  echo "This installer is meant to run inside Termux. Exiting."
  exit 1
fi

pkg update -y || true
pkg upgrade -y || true
pkg install -y git python openssl

python -m pip install --upgrade pip setuptools
python -m pip install -r requirements.txt

PREFIX="$PREFIX"
SHARE_DIR="$PREFIX/share/termux-ai-pro"
BIN_DIR="$PREFIX/bin"

rm -rf "$SHARE_DIR"
mkdir -p "$SHARE_DIR"
cp -r * "$SHARE_DIR/"

cp termux-ai "$BIN_DIR/termux-ai"
chmod +x "$BIN_DIR/termux-ai"
chmod +x "$SHARE_DIR/main.py"

echo "Installation complete. Run: termux-ai"
