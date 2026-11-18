import os
import asyncio

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def send_message():
    bot = Bot(token=TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ Job Radar is working!"
    )

asyncio.run(send_message())
