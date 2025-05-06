from pyrogram import Client, filters
from pyrogram.types import Message
from config import ADMIN_ID
from message_reply import REPLY_STATE

@Client.on_message(filters.private & filters.reply & filters.user(ADMIN_ID))
async def reply_to_user(client, message: Message):
    replied = message.reply_to_message
    if not replied:
        return

    lines = replied.text.splitlines()
    for line in lines:
        if line.strip().startswith("• آیدی عددی:"):
            user_id = int(line.split("`")[1])
            break
    else:
        user_id = REPLY_STATE.get("user_id")

    if user_id:
        try:
            await client.send_message(chat_id=user_id, text=message.text)
            await message.reply("پاسخ با موفقیت ارسال شد.")
        except Exception as e:
            await message.reply(f"خطا در ارسال پاسخ:\n{e}")
