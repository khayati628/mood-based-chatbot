import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_mistralai import ChatMistralAI

load_dotenv()

MODEL_NAME = "open-mistral-7b"
DEFAULT_MODE = "😂 Funny"

MODES = {
    "😡 Angry": {
        "prompt": (
            "You are an angry but entertaining AI agent. "
            "Respond impatiently and sarcastically, but never use "
            "threats or hateful language. Keep replies engaging."
        ),
        "description": "Sarcastic, bold and dramatic.",
    },
    "😂 Funny": {
        "prompt": (
            "You are a very funny AI agent. Respond with humor, "
            "playful jokes and witty remarks. Be friendly and helpful."
        ),
        "description": "Jokes, fun and playful replies.",
    },
    "😢 Sad": {
        "prompt": (
            "You are a sad and emotional AI agent. Speak gently, "
            "with a melancholic tone, while remaining supportive "
            "and helpful."
        ),
        "description": "Emotional, calm and thoughtful.",
    },
}


def get_model():
    if not os.getenv("MISTRAL_API_KEY"):
        raise RuntimeError(
            "MISTRAL_API_KEY is not set. Copy .env.example to .env and add your key."
        )
    return ChatMistralAI(model=MODEL_NAME)


def build_history(mode, messages):
    history = [SystemMessage(content=MODES[mode]["prompt"])]
    for message in messages:
        if message["role"] == "user":
            history.append(HumanMessage(content=message["content"]))
        else:
            history.append(AIMessage(content=message["content"]))
    return history


def get_reply(model, mode, messages):
    response = model.invoke(build_history(mode, messages))
    content = response.content
    return content if isinstance(content, str) else str(content)
