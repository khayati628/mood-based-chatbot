# 🤖 MoodMate AI

A mood-based AI chatbot built with LangChain and Mistral AI. Pick a personality and the bot answers every message in that mood. It ships with a Streamlit web app and a lightweight terminal version.

## Features

- **Three moods**
  - 😡 **Angry**: impatient, sarcastic and dramatic (never hateful)
  - 😂 **Funny**: jokes, wit and playful replies
  - 😢 **Sad**: gentle, melancholic and supportive
- **Streamlit web UI** with a dark theme, mood switcher and "clear conversation" button
- **Terminal CLI** with the same moods
- **Conversation memory** within a session, so the bot remembers earlier messages
- **Shared mood definitions**, so the web app and CLI always behave the same

## Tech Stack

Python 3.10+, [Streamlit](https://streamlit.io), [LangChain](https://www.langchain.com), [Mistral AI](https://mistral.ai) (`open-mistral-7b`), python-dotenv

## Project Structure

```
mood-based-chatbot/
├── app.py            # Streamlit web app
├── cli.py            # Terminal chatbot
├── moods.py          # Mood prompts, model setup and chat logic (shared)
├── styles.css        # Custom styling for the web app
├── requirements.txt
├── .env.example      # Template for your API key
└── .gitignore
```

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/khayati628/mood-based-chatbot
   cd mood-based-chatbot
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Mistral API key**
   ```bash
   cp .env.example .env           # Windows: copy .env.example .env
   ```
   Open `.env` and set your key from the [Mistral Console](https://console.mistral.ai/api-keys/):
   ```env
   MISTRAL_API_KEY="your_actual_api_key_here"
   ```

## Usage

**Web app**
```bash
streamlit run app.py
```

**Terminal**
```bash
python cli.py
```
Choose a mood by number, then chat. Type `0`, `exit` or `quit` to leave.

## Adding Your Own Mood

Add an entry to `MODES` in `moods.py`. It appears in both the web app and the CLI automatically.

```python
"🤓 Nerdy": {
    "prompt": "You are a nerdy AI agent who loves explaining things with fun facts.",
    "description": "Fun facts and geeky explanations.",
},
```

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `MISTRAL_API_KEY is not set` | Create `.env` from `.env.example` and add your key |
| "Unable to get a response" in the web app | Check your API key, internet connection and Mistral quota |
| `ModuleNotFoundError` | Activate your virtual environment and run `pip install -r requirements.txt` |

## Security

Never commit your `.env` file. It is already listed in `.gitignore`. If a key is ever exposed, revoke it in the Mistral Console and create a new one.
