from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from data_base import sqlite_db
from aiogram.types import ReplyKeyboardRemove

'''***********************КЛИЕНТСКАЯ  ЧАСТЬ************************'''


# @dp.message_handler(comands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'У нас большой выбор серёжек ручной работы', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Чтобы общаться с ботом, напишите ему в личку:\nhttps://t.me/Jewelry_JunoBot')


async def jewelry_start_command(message: types.Message):
    await command_start(message)


# @dp.message_handler(commands='Режим работы')
async def jewelry_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')


# @dp.message_handler(commands=['Расположение'])
async def jewelry_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Антона Петрова 170')


# @dp.message_handler(commands=['В наличии'])
async def jewelry_earrings_command(message: types.Message):
    await sqlite_db.sql_read(message)


async def jewelry_reviews_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Отзывы')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(jewelry_open_command, commands=['Режим_работы'])
    dp.register_message_handler(jewelry_place_command, commands=['Расположение'])
    dp.register_message_handler(jewelry_earrings_command, commands=['Серьги'])
    dp.register_message_handler(jewelry_reviews_command, commands=['Отзывы'])
