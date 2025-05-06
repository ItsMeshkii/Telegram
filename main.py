from handlers.start import start_handler
from handlers.messages import message_handler
from handlers.reply import reply_handler
from handlers.block import block_handler
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(start_handler, commands=['start'])
dp.register_message_handler(reply_handler, lambda msg: msg.text.startswith('/reply_'))
dp.register_message_handler(block_handler, lambda msg: msg.text.startswith('/block_') or msg.text.startswith('/unblock_'))
dp.register_message_handler(message_handler, content_types=types.ContentType.ANY)

if __name__ == '__main__':
    executor.start_polling(dp)
