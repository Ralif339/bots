from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (InlineKeyboardButton, 
                           InlineKeyboardMarkup, 
                           Message,
                           CallbackQuery)


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
    
    
@dp.callback_query(F.data == 'button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    some_text = 'Была нажата кнопка 1'
    if callback.message.text != 'Была нажата кнопка 1':
        await callback.message.edit_text(
            text='Была нажата кнопка 1',
            reply_markup=callback.message.reply_markup
            )
    await callback.answer(text='Ура! Нажата кнопка 1',show_alert=True)
    

@dp.callback_query(F.data == 'button_2_pressed')
async def process_button_2_pressed(callback: CallbackQuery):
    some_text = 'Была нажата кнопка 2'
    if callback.message.text != 'Была нажата кнопка 2':
        await callback.message.edit_text(
            text='Была нажата кнопка 2',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Ура! Нажата кнопка 2', show_alert=True)


if __name__ == "__main__":
    dp.run_polling(bot)