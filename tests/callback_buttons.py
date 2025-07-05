from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (InlineKeyboardButton, 
                           InlineKeyboardMarkup, 
                           Message)


BOT_TOKEN = '6551803399:AAF5uGEulD8V28QsSuOSPMeeE3LS6p0Ozcc'
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

button_1 = InlineKeyboardButton(
    text='Кнопка 1',
    callback_data='button_1_pressed'
)

button_2 = InlineKeyboardButton(
    text='Кнопка 2',
    callback_data='button_2_pressed'
)

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_1], [button_2]]
)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки. Нажми на любую!',
        reply_markup=keyboard
    )
    

if __name__ == "__main__":
    dp.run_polling(bot)