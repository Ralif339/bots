from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from keyboards.sss_keyboard import *
from services import *


router = Router()



@router.message(CommandStart())
async def process_start(message: Message):
    await message.answer(text='Привет, это игра "Камень, Ножницы, Бумага"'
                         '\nПодробные правила: /help'
                         '\n\nХочешь сыграть?',
                         reply_markup=create_start_keyboard())
    
    
@router.message(Command('help'))
async def process_help(message: Message):
    await message.answer(text='Игроки одновременно, на счет три, показывают рукой какую-нибудь фигуру из трех возможных: камень (кулак), ножницы (разъединенные указательный и средний пальцы), бумагу (ладонь). Если фигуры одинаковые - ничья. В остальных случаях - бумага побеждает камень, камень побеждает ножницы, а ножницы побеждают бумагу.'
                         '\n\nХочешь сыграть?',
                         reply_markup=create_start_keyboard())
    
    
@router.message(F.text == "Давай!")
async def process_yes_answer(message: Message):
    await message.answer(text="Отлично! Делай свой выбор!",
                         reply_markup=create_choice_keyboard())
    
    
@router.message(F.text == "Не хочу!")
async def process_yes_answer(message: Message):
    await message.answer(text='Хорошо. Если, вдруг, захочешь сыграть - открой клавиатуру и нажми "Давай!"')
    

@router.message(F.text == "Камень")
async def process_stone_btn(message: Message):
    await message.answer(text=process_stone_answer())
    await message.answer(text="Хотите сыграть еще?",
                         reply_markup=create_start_keyboard())
    
    
@router.message(F.text == "Ножницы")
async def process_scissors_btn(message: Message):
    await message.answer(text=process_scissors_answer())
    await message.answer(text="Хотите сыграть еще?",
                         reply_markup=create_start_keyboard())
    
    
@router.message(F.text == "Бумага")
async def process_paper_btn(message: Message):
    await message.answer(text=process_paper_answer())
    await message.answer(text="Хотите сыграть еще?",
                         reply_markup=create_start_keyboard())
    
    
@router.message()
async def process_message(message: Message):
    await message.answer(text='Не понимаю Вас'
                         '\n\nДля дополнительной информации напишите /help')