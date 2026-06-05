import asyncio
from datetime import datetime
import pytz
from telegram import Bot
from telegram.constants import ParseMode

# ✅ உன் Bot Token
BOT_TOKEN = "8910364750:AAEt2LLvAsHJ9M-Le1ufh2_1qK1pi9HbxlA"

# ✅ உன் Channel ID
CHANNEL_ID = -1003967564570

# ✅ Good Morning Message
MESSAGE_TEXT = """🌅 Good Morning, Dear Students! 🌅

⚗️ "Chemistry is not just a subject,
    it's the language of the universe!"

🔬 ஒவ்வொரு element-உம் ஒரு lesson —
    ஒவ்வொரு lesson-உம் உன் future! 🌟

📖 Focus | Learn | Excel

— Pepar Class 🎓"""

# ✅ India Time Zone
IST = pytz.timezone("Asia/Kolkata")

async def send_and_delete():
    bot = Bot(token=BOT_TOKEN)
    now = datetime.now(IST)
    weekday = now.weekday()  # 0=Monday, 2=Wednesday, 4=Friday

     if weekday in [0, 1, 2, 3, 4, 5, 6]: # Mon, Wed, Fri மட்டும்
        # Message அனுப்பு (Forward/Share block)
        msg = await bot.send_message(
            chat_id=CHANNEL_ID,
            text=MESSAGE_TEXT,
            protect_content=True  # 🔒 Forward/Share block
        )
        print(f"✅ Message sent at {now.strftime('%H:%M')} | ID: {msg.message_id}")

        # 4 மணி நேரம் = 14400 seconds (7am to 11am)
        await asyncio.sleep(14400)

        # Message delete
        await bot.delete_message(chat_id=CHANNEL_ID, message_id=msg.message_id)
        print(f"🗑️ Message deleted at 11:00 AM")

async def main():
    IST = pytz.timezone("Asia/Kolkata")
    print("🤖 Bot Started! Waiting for 7:00 AM (Mon/Wed/Fri)...")

    while True:
        now = datetime.now(IST)
        # 7:00 AM ஆகியிருக்கா check பண்ணு
        if now.hour == 10 and now.minute == 15:
            await send_and_delete()
            await asyncio.sleep(60)  # Double send தவிர்க்க
        await asyncio.sleep(30)  # ஒவ்வொரு 30 sec-கும் check

if __name__ == "__main__":
    asyncio.run(main())
