from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMIN_ID, BLOCKED_USERS

@Client.on_message(filters.private & ~filters.command(["start", "login", "message"]))
async def forward_to_admin(client, message):
    user_id = message.from_user.id

    if user_id in BLOCKED_USERS:
        await message.reply_text("شما توسط ادمین بلاک شده‌اید.")
        return

    user = message.from_user
    mention = user.mention
    text = f"""
پیام جدید از کاربر:

• نام: {user.first_name}
• یوزرنیم: @{user.username or 'ندارد'}
• آیدی عددی: `{user.id}`
• لینک: {mention}
• زبان: {user.language_code}
• زمان پیام: {message.date}

متن پیام:
{message.text or '[بدون متن]'}
"""

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("پاسخ", callback_data=f"reply_{user_id}"),
            InlineKeyboardButton("بلاک", callback_data=f"block_{user_id}")
        ]
    ])

    await client.send_message(chat_id=ADMIN_ID, text=text, reply_markup=buttons)
    await message.reply_text("پیام شما با موفقیت برای ادمین ارسال شد.")
