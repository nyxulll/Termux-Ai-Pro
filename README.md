# Termux-AI-Pro

A clean, modern, beginner-friendly AI client for **Termux** with a beautiful terminal UI, Markdown responses, and simple API setup.

![Termux AI Banner](https://raw.githubusercontent.com/nyxulll/Termux-AI-Pro/main/banner.png)

---

## 🌟 Features

* **Friendly first-run setup**

  * "Welcome to Termux-AI-Pro! Please enter your API key" prompt
  * Auto‑saves your key (no need to re-enter)
* **GPT-style chat experience** inside Termux
* **Beautiful UI** using Rich (Markdown, panels, colors)
* **Simple folder structure** — easy to modify & build on
* **Stable installer script**
* **Works on any Android device using Termux**

---

## 📦 Installation

Open Termux and run:

```bash
pkg update -y
pkg install git python -y

git clone https://github.com/nyxulll/Termux-Ai-Pro
cd Termux-Ai-Pro

chmod +x install.sh
./install.sh
```

After installation, start the app:

```bash
termux-ai
```

---

## 🔑 First Run (API Key Setup)

On your very first run, Termux-AI-Pro will show:

```
Welcome to Termux-AI-Pro!
Please enter your OpenAI API key (you can paste it here)
:
```

Paste your API key and press Enter.
It will be saved automatically in:

```
~/.config/termux-ai-pro/config.json
```

You will **never** be asked again unless you delete the file.

---

## 🧠 Usage

After running:

```bash
termux-ai
```

Just start typing questions:

```
You: explain what a linux kernel is
```

AI responds with Markdown‑formatted, clean output.

Press **Ctrl + C** to exit.

---

## 📁 Project Structure

```
Termux-Ai-Pro/
 ├── main.py                 # Main chat UI
 ├── config.py               # Clean config system
 ├── install.sh              # Installer
 ├── termux-ai               # Launcher
 ├── requirements.txt        # Python dependencies
 ├── providers/
 │     └── openai_provider.py  # Handles OpenAI API
 └── README.md
```

---

## 🧩 Adding More Providers (Gemini, Claude, etc.)

The project is designed to be modular.
To add a provider:

1. Create a new file in `providers/`
2. Add your provider class
3. Import it in `main.py`

I can help you add:

* Google Gemini
* Anthropic Claude
* DeepSeek
* Local models

Just ask.

---

## 🛠 Requirements

* Termux (latest)
* Python 3
* Internet connection
* OpenAI API key (for now)

---

## 📜 License

MIT License — free to modify, use, and improve.

---

## ❤️ Credits

Created by **nyxulll**.


Made with ❤️ for the Termux community.

