import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from keyboards.main_menu import set_main_menu


logger = logging.getLogger(__name__)


async def main():
    config: Config = load_config()
    
    logging.basicConfig(
        level=config.log_settings.level,
        format=config.log_settings.format
    )
    
    logger.info('Starting bot')
    
    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    dp = Dispatcher()
    
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    
    await set_main_menu(bot)
    
    await dp.start_polling(bot)
    
asyncio.run(main())