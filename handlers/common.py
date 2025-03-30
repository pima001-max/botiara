from aiogram import types, Router
from aiogram.filters import Command

# Создаем отдельный router для этих обработчиков.
common_router = Router()


@common_router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Это общая команда /start.")
