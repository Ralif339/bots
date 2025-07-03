from aiogram import Bot, Dispatcher
import asyncio
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import Config, load_config
from handlers import user


async def main():
    config: Config = load_config()
    
    logging.basicConfig(level=config.log_settings.level,
                        format=config.log_settings.format)
    
    bot = Bot(config.tg_bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    dp = Dispatcher()
    
    dp.include_router(user.router)
    
    await dp.start_polling(bot)
    
asyncio.run(main())