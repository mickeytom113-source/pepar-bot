import asyncio
from datetime import datetime
import pytz
from telegram import Bot

BOT_TOKEN = "8910364750:AAEt2LLvAsHJ9M-Le1ufh2_1qK1pi9HbxlA"
CHANNEL_ID = -1003967564570

MESSAGE_TEXT = """🌅 Good Morning, Dear Students! 🌅

⚗️ "Chemistry is not just a subject,
    it's the language of the universe!"

🔬 ஒவ்வொரு element-உம் ஒரு lesson —
    ஒவ்வொரு lesson-உம் உன் future! 🌟

📖 Focus | Learn | Excel

— Pepar Class 🎓"""

IST = pytz.timezone("Asia/Kolkata")

async def send_and_delete():
    bot = Bot(token=BOT_TOKEN)
    msg = await bot.send_message(
        chat_id=CHANNEL_ID,
        text=MESSAGE_TEXT,
        protect_content=True
    )
    print(f"✅ Message sent! ID: {msg.message_id}")
    await asyncio.sleep(14400)
    await bot.delete_message(chat_id=CHANNEL_ID, message_id=msg.message_id)
    print("🗑️ Message deleted!")

async def main():
    print("🤖 Bot Started!")
    while True:
        now = datetime.now(IST)
        weekday = now.weekday()
        if weekday in [0, 1, 2, 3, 4, 5, 6]:
            if now.hour == 7 and now.minute == 0:
                await send_and_delete()
                await asyncio.sleep(60)
        await asyncio.sleep(30)

if __name__ == "__main__":
    asyncio.run(main())
