#!/bin/bash
set -e

echo "Installing Termux-AI-Pro..."

pkg update -y
pkg install -y python git

pip install --upgrade pip
pip install -r requirements.txt

# Install launcher
cp termux-ai $PREFIX/bin/termux-ai
chmod +x $PREFIX/bin/termux-ai

# Copy project files
mkdir -p $PREFIX/share/termux-ai-pro
cp -r * $PREFIX/share/termux-ai-pro

echo "Installation complete!"
echo "Start the app by typing: termux-ai"
