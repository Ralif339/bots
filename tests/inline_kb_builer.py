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
    text='Отправь кошку',
    callback_data='cat_btn_pressed'
)

btn2 = InlineKeyboardButton(
    text='Отправь собаку',
    callback_data='dog_btn_pressed'
)

inline_kb_builder = InlineKeyboardBuilder()

inline_kb_builder.row(btn1, btn2, width=2)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Выберите кнопку',
        reply_markup=inline_kb_builder.as_markup()
    )
    
    
@dp.callback_query(F.data == 'cat_btn_pressed')
async def process_cat_btn_pressed(callback: CallbackQuery):
    await callback.message.answer('🐈')
    

@dp.callback_query(F.data == 'dog_btn_pressed')
async def process_dog_btn_pressed(callback: CallbackQuery):
    await callback.message.answer('🐕')
    

dp.run_polling(bot)