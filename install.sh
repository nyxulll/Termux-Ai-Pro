#!/data/data/com.termux/files/usr/bin/bash

echo "📦 Installing Termux-AI-Pro dependencies..."

# Update packages
pkg update -y
pkg upgrade -y

# Install Python & essential packages
pkg install -y python python-pip git

# Upgrade pip essentials
pip install --upgrade pip setuptools wheel

# Install required Python modules WITHOUT Rust builds (avoids jiter error)
echo "📥 Installing Python requirements..."
pip install --no-build-isolation --no-cache-dir -r requirements.txt

echo "✅ Installation complete!"
echo "Run the app with: python main.py"
