from aiogram import types, Router

# Создаем router для пользовательских команд.
user_router = Router()


@user_router.message(lambda message: message.text == "Пользователь")
async def user_mode(message: types.Message):
    # Логика для работы с пользователями
    await message.answer("Вы в пользовательском режиме")
