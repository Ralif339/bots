from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (ReplyKeyboardMarkup,
                           ReplyKeyboardRemove, 
                           KeyboardButton)


def create_start_keyboard() -> ReplyKeyboardMarkup:
    kb_builder = ReplyKeyboardBuilder()
    
    yes_btn = KeyboardButton(text="Давай!")
    no_btn = KeyboardButton(text="Не хочу!")

    kb_builder.row(yes_btn, no_btn)
    return kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def create_choice_keyboard() -> ReplyKeyboardMarkup:
    kb_builder = ReplyKeyboardBuilder()
    
    stone_btn = KeyboardButton(text="Камень")
    paper_btn = KeyboardButton(text="Бумага")
    scissors_btn = KeyboardButton(text="Ножницы")
    
    kb_builder.row(stone_btn, paper_btn, scissors_btn)
    
    return kb_builder.as_markup(resize_keyboard=True)