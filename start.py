from pyrogram import Client, filters
from config import ADMIN_ID

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    user = message.from_user
    name = user.first_name
    mention = user.mention

    text = f"""
┏━━━━━━━━━━━━┓
  خوش‌اومدی {mention}  
┗━━━━━━━━━━━━┛

این ربات برای ارتباط با مدیریت ساخته شده.
پیام‌تو بفرست تا به دست ادمین برسه.
"""

    await message.reply_text(text)

    # اطلاع‌رسانی به ادمین
    await client.send_message(
        ADMIN_ID,
        f"✅ کاربر جدید استارت زد:\n\n"
        f"• نام: {user.first_name}\n"
        f"• یوزرنیم: @{user.username or 'ندارد'}\n"
        f"• آیدی عددی: `{user.id}`\n"
        f"• لینک: {mention}"
    )
