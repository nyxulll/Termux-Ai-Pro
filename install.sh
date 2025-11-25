#!/bin/bash

# Termux AI Pro Installer
# Installs main.py from the CURRENT directory to the system path

PREFIX="/data/data/com.termux/files/usr"
INSTALL_DIR="$PREFIX/share/termux-ai-pro"
BIN_DIR="$PREFIX/bin"
EXECUTABLE_NAME="termux-ai"

# Colors
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RESET='\033[0m'

clear
echo -e "${CYAN}=================================${RESET}"
echo -e "${CYAN}   Termux AI Pro Installer      ${RESET}"
echo -e "${CYAN}=================================${RESET}"
echo ""

# 1. Update and Install Dependencies
echo -e "${YELLOW}[*] Updating package lists...${RESET}"
pkg update -y > /dev/null 2>&1

echo -e "${YELLOW}[*] Installing Python and Pip...${RESET}"
pkg install python -y > /dev/null 2>&1

echo -e "${YELLOW}[*] Installing Python libraries...${RESET}"
# Try installing from requirements, fallback to manual list
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt --quiet
else
    pip install rich requests --quiet
fi

# 2. Create Installation Directory
echo -e "${YELLOW}[*] Setting up directory structure...${RESET}"
if [ -d "$INSTALL_DIR" ]; then
    rm -rf "$INSTALL_DIR"
fi
mkdir -p "$INSTALL_DIR"

# 3. Move the Application
if [ -f "main.py" ]; then
    cp main.py "$INSTALL_DIR/main.py"
    echo -e "${GREEN}✔ Core files copied.${RESET}"
else
    echo -e "\033[0;31mError: main.py not found! Are you in the repo folder?${RESET}"
    exit 1
fi

# 4. Create the Binary Executable
echo -e "${YELLOW}[*] Creating global command '${EXECUTABLE_NAME}'...${RESET}"
echo "#!$PREFIX/bin/bash" > "$BIN_DIR/$EXECUTABLE_NAME"
echo "python3 $INSTALL_DIR/main.py \"\$@\"" >> "$BIN_DIR/$EXECUTABLE_NAME"
chmod +x "$BIN_DIR/$EXECUTABLE_NAME"

# 5. Success Message
echo ""
echo -e "${GREEN}✔ Installation Complete!${RESET}"
echo -e "Start the AI from anywhere by typing:"
echo -e "${CYAN}   $EXECUTABLE_NAME${RESET}"
echo ""
