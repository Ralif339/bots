import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from keyboards.main_menu import set_main_menu
from services.file_handling import prepare_book
from database.database import init_db


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
    
    logger.info("Preparing the book...")
    book = prepare_book("C:\\Users\\sarim\\OneDrive\\Рабочий стол\\python\\book_bot\\books\\book.txt")
    logger.info("The book is uploaded. Total pages: %d", len(book))
    
    db: dict = init_db()
    
    dp.workflow_data.update(book=book, db=db)
    
    dp.include_router(user_handlers.user_router)
    dp.include_router(other_handlers.other_router)
    
    await set_main_menu(bot)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
asyncio.run(main())