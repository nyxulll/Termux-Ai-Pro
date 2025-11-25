

# 🤖 Termux AI Pro

### **The Ultimate CLI AI Client for Termux**

> Chat with GPT-4, Gemini, DeepSeek, and Local Models — all inside a beautiful, rich terminal interface.

Termux AI Pro is a full-featured Python application designed to replace basic shell scripts.
It brings a modern AI chat experience to Termux with **Markdown rendering**, **streaming responses**, and **multi-provider support**.

---

## ✨ Features

### 🎨 Beautiful UI

Powered by the **Rich** library — supports Markdown, code blocks, tables, lists, and more.

### ⚡ Real-time Streaming

Responses appear instantly as the AI types.

### 🌍 Universal Model Support

Out of the box integration with:

* **OpenRouter** (DeepSeek, Claude 3, Llama 3, etc.)
* **Google Gemini** (Free tier available)
* **OpenAI** (GPT-4o, GPT-3.5)
* **Local / Ollama** (Run on your PC or local server)

### 💾 Session Memory

The AI remembers earlier messages within the current conversation.

### ⚙️ Easy Configuration

Includes a settings menu to manage API keys, models, and providers — no file editing needed.

---

## 🚀 Installation

> ⚠️ **IMPORTANT:**
> Replace **`YOUR_USERNAME`** and **`Termux-AI-Pro`** with your actual GitHub username and repository name.

---

### **Option 1 — Standard Clone & Install (Recommended)**

Install Git & Python:

```bash
pkg update && pkg upgrade -y
pkg install git python -y
```

Clone your repository:

```bash
git clone https://github.com/YOUR_USERNAME/Termux-AI-Pro.git
cd Termux-AI-Pro
```

Run installer:

```bash
chmod +x install.sh
./install.sh
```

---

### **Option 2 — One-Line Installer**

Run directly from Termux:

```bash
curl -sL https://raw.githubusercontent.com/YOUR_USERNAME/Termux-AI-Pro/main/install.sh | bash
```

---

## 🎮 Usage

Launch the AI from anywhere:

```bash
termux-ai
```

### **In-Chat Commands**

| Command           | Description               |
| ----------------- | ------------------------- |
| `menu`            | Open settings menu        |
| `clear`           | Clear conversation memory |
| `exit`            | Quit application          |
| *(anything else)* | Send message to AI        |

---

## 🔑 Setup & Configuration

The first run will prompt you to enter your API key.

### **Where to Get API Keys**

* **OpenRouter** — Free + paid (recommended)
* **Google AI Studio** — Free Gemini keys
* **OpenAI Platform** — Paid

### **To Enter Your Key**

1. Run `termux-ai`
2. Type `menu`
3. Select **[2] Edit Configuration**
4. Choose provider (OpenRouter, Gemini, etc.)
5. Paste your API key

---

## 🏠 Using Local AI (Ollama)

You can connect Termux to an **Ollama server** running on your PC.

### **Step 1 — Make Ollama Network-Accessible**

On your PC:

```bash
export OLLAMA_HOST=0.0.0.0
```

### **Step 2 — Configure Termux AI**

1. Run `termux-ai`
2. Type `menu`
3. Select **[1] Switch Provider → Local (Ollama)**
4. Go to **[2] Edit Configuration**
5. Set Base URL:

```
http://YOUR_PC_IP_ADDRESS:11434/v1
```

6. Set Model to your installed model (e.g., `llama3`)

---

## 🛠️ Troubleshooting

### **❌ “Command not found”**

Run:

```bash
hash -r
```

Or restart Termux.

### **❌ Connection Errors**

* Check your API key in the menu
* Ensure internet is working
* If using remote models, verify credit/access
* For Ollama, ensure the server is reachable on your network

### **Config File Location**

```
~/.config/termux_ai_pro/config.json
```

---

## 📝 License

This project is licensed under the **MIT License**.

