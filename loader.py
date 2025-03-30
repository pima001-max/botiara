from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties  # Добавлен импорт DefaultBotProperties
from utils.db.storage import DatabaseManager

from data import config

# Исправленный код инициализации бота
bot = Bot(
    token=config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # Передаем parse_mode через DefaultBotProperties
)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
db = DatabaseManager('data/database.db')
