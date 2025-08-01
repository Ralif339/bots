import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)


bot = Bot('6551803399:AAHxAkdTW2uhs90kZ1rJL-Dp7AudTNhNAx4')
dp = Dispatcher()


class GoodsCallbackFactory(CallbackData, prefix='goods'):
    category_id: int
    subcategory_id: int
    item_id: int
    

button_1 = InlineKeyboardButton(
    text='Категория 1',
    callback_data=GoodsCallbackFactory(
        category_id=1, subcategory_id=0, item_id=0
    ).pack()
)

button_2 = InlineKeyboardButton(
    text='Категория 2',
    callback_data=GoodsCallbackFactory(
        category_id=2, subcategory_id=0, item_id=0
    ).pack()
)

markup = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2]])


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text="Вот такая клавиатура", 
                         reply_markup=markup)
    
    
@dp.callback_query()
async def process_any_inline_button_press(callback: CallbackQuery):
    print(callback.model_dump_json(indent=4, exclude_none=True))
    await callback.answer()
    
    
if __name__ == "__main__":
    dp.run_polling(bot)