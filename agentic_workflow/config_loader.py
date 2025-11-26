import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="app.env")

#GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#LLM_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_LLM_MODEL = os.getenv("OPENAI_LLM_MODEL", "gpt-4o-mini")
