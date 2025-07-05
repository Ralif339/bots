from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton,
                           Message,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder


BOT_TOKEN = '6551803399:AAF5uGEulD8V28QsSuOSPMeeE3LS6p0Ozcc'
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

kb_builder = ReplyKeyboardBuilder()
buttons_1 = [KeyboardButton(text=f"Кнопка {i + 1}") for i in range(12)]
buttons_2 = [KeyboardButton(text=f"Кнопка {i + 1}") for i in range(10)]

kb_builder.add(*buttons_1)

kb_builder.adjust(1, 3)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text="Чего коши боятся больше?",
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )
    

@dp.message(F.text == "Собак🐶")
async def process_dog_answer(message: Message):
    await message.answer(
        text='Да, несомненно, кошки боятся собак. '
             'Но вы видели как они боятся огурцов?'
    )
    

@dp.message(F.text == "Огурцов🥒")
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='Да, иногда кажется, что огурцов '
             'кошки боятся больше',
    )
    
    
if __name__ == '__main__':
    dp.run_polling(bot)