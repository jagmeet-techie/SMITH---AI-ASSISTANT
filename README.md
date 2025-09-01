# 🧠 Chatmeet — Your AI Voice Assistant

Chatmeet is a smart voice-controlled desktop assistant built using Python. Designed to function like Siri or Alexa, SMITH can understand your voice, respond like a human using Cohere's NLP model, and perform practical system-level tasks such as opening Chrome, VS Code, or directories — all hands-free.

## 🔧 Features

- 🎙️ Voice recognition (English-based)
- 🗣️ Text-to-speech responses using `pyttsx3`
- 🧠 Natural conversation using Cohere AI
- 💻 System automation: open VS Code, Chrome, Downloads, D drive
- 🛑 Wake/sleep commands like "stop smith" or "goodbye"
- 🧪 Simple and clean CLI-based interaction

## 🧱 Tech Stack

- Python 3
- `speech_recognition`
- `pyttsx3`
- `cohere`
- `subprocess`, `os`

## 🚀 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/jagmeet-techie/SMITH---AI-ASSISTANT.git
   cd SMITH---AI-ASSISTANT
2.pip install -r requirements.txt
Add your Cohere API Key
Replace the dummy key in smith.py with your actual Cohere API key:


3.COHERE_API_KEY = "your-cohere-api-key"
Run the assistant

4.python smith.py
