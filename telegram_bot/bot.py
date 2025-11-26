from telegram import Bot
from dotenv import load_dotenv
import os
import asyncio


load_dotenv(dotenv_path="../app.env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=TELEGRAM_BOT_TOKEN)


async def send_telegram_bot_msg(message : str) :
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    return {"status" : "message sent"}

if __name__ == "__main__" :
    message = "You are my personal chef assistant."
    response =  asyncio.run(send_telegram_bot_msg(message))
    print(response)