from aiogram.types import Message
from aiogram.filters import BaseFilter
from data.config import ADMINS


class IsUser(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id not in ADMINS
