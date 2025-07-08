from aiogram import Bot, Dispatcher, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (InlineKeyboardButton, 
                           InlineKeyboardMarkup, 
                           Message,
                           CallbackQuery)
from aiogram.filters import CommandStart



bot = Bot('6551803399:AAF5uGEulD8V28QsSuOSPMeeE3LS6p0Ozcc')

dp = Dispatcher()


btn1 = InlineKeyboardButton(
    text='Узнать свой id',
    callback_data='my_id_btn_pressed'
)

inline_kb_builder = InlineKeyboardBuilder()

inline_kb_builder.row(btn1)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Нажмите на кнпоку'
        f'\nВаш айди: {message.from_user.id}' 
        f'\nАйди чата: {message.chat.id}',
        reply_markup=inline_kb_builder.as_markup()
    )
    
    
@dp.callback_query(F.data == 'my_id_btn_pressed')
async def process_cat_btn_pressed(callback: CallbackQuery):
    await callback.message.answer(str(callback.from_user.id) + '\n' + str(callback.message.chat.id))
    

dp.run_polling(bot)