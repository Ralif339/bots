from aiogram.types import (ReplyKeyboardMarkup, 
                           KeyboardButton, 
                           KeyboardButtonPollType,
                           Message)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

BOT_TOKEN = '6551803399:AAF5uGEulD8V28QsSuOSPMeeE3LS6p0Ozcc'
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

kb_builder = ReplyKeyboardBuilder()

contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)

geo_btn = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)

poll_btn = KeyboardButton(
    text='Создать опрос/викторину',
    request_poll=KeyboardButtonPollType()
)

kb_builder.row(contact_btn, geo_btn, poll_btn, width=1)

keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True,
)

@dp.message(CommandStart())
async def process_start_bot(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=keyboard
    )
    

if __name__ == '__main__':
    dp.run_polling(bot)