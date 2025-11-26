# 🤖 Termux AI Pro
The Ultimate CLI AI Client for Termux.

> Chat with GPT‑4, Gemini, DeepSeek, Claude, and even local models — all inside Termux with a beautiful terminal UI.

---

## ✨ Features

### 🎨 Beautiful UI
- Built with the **Rich** Python library
- Clean chat bubbles, markdown rendering, syntax highlighting, and smooth scrolling

### 🔌 Universal AI Support
Use **any** provider:
- OpenAI (GPT‑3.5, GPT‑4, GPT‑4o, etc.)
- Google Gemini
- DeepSeek
- Anthropic Claude
- Local models (via LMStudio / Ollama API)
- Custom API endpoints

### ⚡ Fast Streaming Replies
- Real‑time streaming
- Auto‑wrap

### 📁 Chat Management
- Save / load chats
- Export conversations to Markdown
- Custom system prompts

### 🛠 Built for Termux
- 100% Python
- Zero-bloat
- Works on Android

---

## 📦 Installation

### 1. Install Termux packages
```
pkg update && pkg upgrade
pkg install python git
pip install rich requests prompt_toolkit
```

### 2. Clone this repo
```
git clone https://github.com/nyxulll/Termux-Ai-Pro.git
cd Termux-Ai-Pro
```

### 3. Add your API key(s)
Edit your config file:
```
nano config.json
```
Example:
```json
{
  "provider": "openai",
  "api_key": "YOUR_KEY",
  "model": "gpt-4o-mini"
}
```

### 4. Run it
```
python main.py
```

---

## 📙 Usage
- Type your message and press **Enter**
- Use `/provider` to switch providers
- Use `/model` to switch models
- Use `/save` and `/load` to manage chats
- Use `/clear` to clear screen

---

## 🧩 Supported Commands
```
/help       Show help menu
/provider   Change AI provider
/model      Change model
/save       Save chat history
/load       Load chat history
/clear      Clear terminal
/exit       Quit
```

---

## 📚 Screenshots
*(Add your screenshots here)*

---

## 🛠 Development
Pull requests are welcome.
If you want new features, open an issue.

---

## ⭐ Support
If you like this project, consider starring ⭐ the repo!

