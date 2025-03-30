from aiogram import types, Router

# Создаем router для обработчиков админских команд.
admin_router = Router()


@admin_router.message(lambda message: message.text == "Админ")
async def admin_mode(message: types.Message):
    # Логика для работы с админами
    await message.answer("Админский режим включен")
