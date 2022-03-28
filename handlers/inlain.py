from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


answ = dict()


# Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton('Ссылка2', url='https://google.com')
urlkb.add(urlButton, urlButton2)


@dp.message_handler(command='ссылки')
async def url_command(message: types.Message):
    await message.answer('Ссылочки: ', reply_markup=urlkb)


inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='Like_1'),
                                             InlineKeyboardButton(text='He Like', callback_data='Like_-1'))


@dp.callback_query_handlers(Text(startswith='Like'))
async def www_call(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)


executor.start_polling(dp, skip_updates=True)

