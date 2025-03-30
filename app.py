from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from logging import basicConfig, INFO
from data import config
from handlers import common_router, admin_router, user_router
from DatabaseManager import DatabaseManager

user_message = 'Пользователь'
admin_message = 'Админ'

# Инициализация бота
bot = Bot(
    token=config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

storage = MemoryStorage()
dp = Dispatcher(storage=storage)  # Глобальный dispatcher

# Подключение базы данных
db = DatabaseManager('data/database.db')
db.connect()  # Устанавливаем соединение при запуске

ADMINS = []


@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=user_message), KeyboardButton(text=admin_message)]
        ],
        resize_keyboard=True
    )

    await message.answer('''Привет! 👋

🤖 Я бот-магазин по подаже товаров любой категории.

🛍️ Чтобы перейти в каталог и выбрать приглянувшиеся 
товары воспользуйтесь командой /menu.

❓ Возникли вопросы? Не проблема! Команда /sos поможет 
связаться с админами, которые постараются как можно быстрее откликнуться.
    ''', reply_markup=markup)


@dp.message(lambda message: message.text == admin_message)
async def admin_mode(message: types.Message):
    cid = message.chat.id
    if cid not in ADMINS:
        ADMINS.append(cid)
    await message.answer('Включен админский режим.', reply_markup=ReplyKeyboardRemove())


@dp.message(lambda message: message.text == user_message)
async def user_mode(message: types.Message):
    cid = message.chat.id
    if cid in ADMINS:
        ADMINS.remove(cid)
    await message.answer('Включен пользовательский режим.', reply_markup=ReplyKeyboardRemove())


async def on_startup():
    basicConfig(level=INFO)
    print("Бот стартует")


async def main() -> None:
    dp.include_router(common_router)
    dp.include_router(admin_router)
    dp.include_router(user_router)

    await on_startup()
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
