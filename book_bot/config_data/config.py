from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admins_id: list[int]
    
@dataclass
class LogSettings:
    level: str
    format: str
    
@dataclass
class Config:
    tg_bot: TgBot
    log_settings: LogSettings
    
    
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admins_id=list(map(int, env.list('ADMIN_IDS')))
        ),
        log_settings=LogSettings(
            level=env('LOG_LEVEL'),
            format=env('LOG_FORMAT')
        )
    )