from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

BOT_TOKEN = '6551803399:AAF5uGEulD8V28QsSuOSPMeeE3LS6p0Ozcc'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def set_main_menu(bot: Bot):
    
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка о работе ботика'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/payments',
                   description='Платежи')
    ]
    
    await bot.set_my_commands(main_menu_commands)
    

dp.startup.register(set_main_menu)

dp.run_polling(bot)