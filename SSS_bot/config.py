from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    
    
@dataclass
class LogSettings:
    level: str
    format: str
    
@dataclass
class Config:
    tg_bot: TgBot
    log_settings: LogSettings
    

def load_config(path: str | None = None):
    env = Env()
    env.read_env()
    
    tg_bot = TgBot(token=env('BOT_TOKEN'))
    log_settings = LogSettings(level=env('LOG_LEVEL'),
                               format=env('LOG_FORMAT'))
    
    return Config(tg_bot=tg_bot,
                  log_settings=log_settings)