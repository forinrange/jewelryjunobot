import json
import string

from aiogram import types, Dispatcher


# @dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрешены')
        await message.delete()

    # if message.text == "Привет" or "привет":
    #     await message.answer('Привет! я bot telegram. Меня написал Николай Чумак!')
    #     await message.reply(message.text)
    #     await bot.send_message(message.from_user.id, message.text)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
