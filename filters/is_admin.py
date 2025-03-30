from aiogram.types import Message
from data.config import ADMINS


class IsAdmin:
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in ADMINS

