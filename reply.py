from pyrogram import Client, filters
from pyrogram.types import Message
import json
import os

# فایل موقتی برای نگهداری پیام‌هایی که قراره ریپلای بشن
REPLY_FILE = "reply_data.json"

# هندل کردن پیام ادمین وقتی روی دکمه "پاسخ" کلیک کرده
@Client.on_callback_query(filters.regex(r"^reply_\d+$"))
async def handle_reply_button(client, callback_query):
    user_id = callback_query.data.split("_")[1]
    with open(REPLY_FILE, "w") as f:
        json.dump({"user_id": user_id, "admin_id": callback_query.from_user.id}, f)
    await callback_query.message.reply("پیام خود را برای کاربر ارسال کنید.")
    await callback_query.answer()

# دریافت پیام ادمین بعد از زدن دکمه "پاسخ"
@Client.on_message(filters.private & filters.text)
async def send_reply_message(client: Client, message: Message):
    if not os.path.exists(REPLY_FILE):
        return

    with open(REPLY_FILE, "r") as f:
        data = json.load(f)

    if message.from_user.id != data["admin_id"]:
        return

    try:
        await client.send_message(int(data["user_id"]), f"پیام مدیر:\n{message.text}")
        await message.reply("پاسخ شما ارسال شد.")
        os.remove(REPLY_FILE)
    except Exception as e:
        await message.reply(f"خطا در ارسال پیام: {e}")
