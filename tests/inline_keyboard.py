from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, Message

BOT_TOKEN = '6551803399:AAF5uGEulD8V28QsSuOSPMeeE3LS6p0Ozcc'
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

url_button1 = InlineKeyboardButton(
    text='Курс "Телеграм-боты на Python и AIOgram"',
    url='https://stepik.org/120924'
)

url_button2 = InlineKeyboardButton(
    text='Документация Telegram Bot API',
    url='https://core.telegram.org/bots/api'
)


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button1], [url_button2]]
)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки с параметром "url"',
        reply_markup=keyboard
    )
    
    
if __name__ == '__main__':
    dp.run_polling(bot)