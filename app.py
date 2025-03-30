from aiogram import Bot, Dispatcher, types 
from aiogram.enums import ParseMode  # Исправлено
from aiogram.fsm.storage.memory import MemoryStorage  # Исправлено
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton  # Исправлено
from aiogram.filters.command import Command  # Исправлено
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from aiogram.client.bot import DefaultBotProperties  # Новый импорт
from logging import basicConfig, INFO

from data.config import ADMINS
from utils.db.storage import DatabaseManager

user_message = 'Пользователь'
admin_message = 'Админ'

# Инициализация бота, хранилища и диспетчера
bot = Bot(
    token="7447558856:AAHjeaokhtisccDCyXVN2RagyGsyFPCywAY",
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # Исправлено
)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
db = DatabaseManager('data/database.db')


@dp.message(Command(commands=["start"]))  # Исправлено
async def cmd_start(message: types.Message):
    # Создаем клавиатуру правильно, добавляя кнопки через KeyboardButton
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=user_message), KeyboardButton(text=admin_message)]
        ],
        resize_keyboard=True
    )

    await message.answer('''Привет! 👋

🤖 Я бот-магазин по подаже товаров любой категории.

🛍️ Чтобы перейти в каталог и выбрать приглянувшиеся 
товары возпользуйтесь командой /menu.

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
    db.create_tables()


async def main():
    # Регистрируем middlewares, если нужно
    dp.message.middleware(CallbackAnswerMiddleware())
    await on_startup()

    print("Бот запущен!")
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
