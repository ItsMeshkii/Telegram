from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
import json
import os

BLOCKED_USERS_FILE = "blocked_users.json"

def load_blocked_users():
    if os.path.exists(BLOCKED_USERS_FILE):
        with open(BLOCKED_USERS_FILE, "r") as f:
            return json.load(f)
    return []

def save_blocked_users(users):
    with open(BLOCKED_USERS_FILE, "w") as f:
        json.dump(users, f)

@Client.on_callback_query(filters.regex(r"^(block|unblock)_\d+$"))
async def handle_block_unblock(client: Client, callback_query: CallbackQuery):
    action, user_id = callback_query.data.split("_")
    user_id = int(user_id)
    blocked_users = load_blocked_users()

    if action == "block":
        if user_id not in blocked_users:
            blocked_users.append(user_id)
            save_blocked_users(blocked_users)
            await callback_query.answer("کاربر بلاک شد.", show_alert=True)
        else:
            await callback_query.answer("کاربر از قبل بلاک بوده.", show_alert=True)

    elif action == "unblock":
        if user_id in blocked_users:
            blocked_users.remove(user_id)
            save_blocked_users(blocked_users)
            await callback_query.answer("کاربر آنبلاک شد.", show_alert=True)
        else:
            await callback_query.answer("کاربر قبلاً آنبلاک شده.", show_alert=True)
