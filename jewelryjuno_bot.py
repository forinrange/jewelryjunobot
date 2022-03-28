from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other
from data_base import sqlite_db

b10 = KeyboardButton('/start')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b10)


async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
