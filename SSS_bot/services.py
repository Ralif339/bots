from random import randint

bot_choices = {1: "Камень",
               2: "Бумага",
               3: "Ножницы"}

def get_bot_choice():
    return bot_choices[randint(1, 3)]

def process_stone_answer() -> str:
    bot_choice = get_bot_choice()
    
    if bot_choice == "Камень":
        bot_answer = f"{bot_choice}" \
            "\n\nНичья!"
    elif bot_choice == "Ножницы":
        bot_answer = f"{bot_choice}" \
            "\n\nВы выиграли!"
    else:
        bot_answer = f"{bot_choice}" \
            "\n\nВы проиграли!"
            
    return bot_answer
            
        
def process_scissors_answer() -> str:
    bot_choice = get_bot_choice()
    
    if bot_choice == "Ножницы":
        bot_answer = f"{bot_choice}" \
            "\n\nНичья!"
    elif bot_choice == "Бумага":
        bot_answer = f"{bot_choice}" \
            "\n\nВы выиграли!"
    else:
        bot_answer = f"{bot_choice}" \
            "\n\nВы проиграли!"
            
    return bot_answer
            
            
def process_paper_answer() -> str:
    bot_choice = get_bot_choice()
    
    if bot_choice == "Бумага":
        bot_answer = f"{bot_choice}" \
            "\n\nНичья!"
    elif bot_choice == "Камень":
        bot_answer = f"{bot_choice}" \
            "\n\nВы выиграли!"
    else:
        bot_answer = f"{bot_choice}" \
            "\n\nВы проиграли!"
            
    return bot_answer