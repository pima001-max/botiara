from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from filters import IsAdmin, IsUser

router = Router()


catalog = '🛍️ Каталог'
cart = '🛒 Корзина'
delivery_status = '🚚 Статус заказа'

settings = '⚙️ Настройка каталога'
orders = '🚚 Заказы'
questions = '❓ Вопросы'


@router.message(IsAdmin(), Command('menu'))
async def admin_menu(message: Message):
    # Создаем клавиатуру с кнопками для администратора
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        selective=True,
        keyboard=[
            [KeyboardButton(text=settings)],  # Указываем "text" явно
            [KeyboardButton(text=questions), KeyboardButton(text=orders)]  # Указываем "text" для каждой кнопки
        ]
    )

    await message.answer('Меню', reply_markup=markup)


@router.message(IsUser(), Command('menu'))
async def user_menu(message: Message):
    # Создаем клавиатуру с кнопками для пользователя
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        selective=True,
        keyboard=[
            [KeyboardButton(text=catalog)],  # Указываем "text" явно
            [KeyboardButton(text=cart)],  # Указываем "text" для каждой кнопки
            [KeyboardButton(text=delivery_status)]  # Указываем "text" для каждой кнопки
        ]
    )

    await message.answer('Меню', reply_markup=markup)


@router.message()
async def example_handler(message):
    await message.answer("Это пример обработчика в модуле menu.")


@router.message()
async def handle_user_message(message):
    await message.answer("Это сообщение обработано 'user.menu'.")
