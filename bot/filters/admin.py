from aiogram.types import Message
from aiogram.filters import BaseFilter
from asgiref.sync import sync_to_async
from bot.models import TelegramAdmin


class AdminFilter(BaseFilter):
    """Allows only administrators for specified handlers."""

    async def __call__(self, message: Message) -> bool:
        if not message.from_user:
            return False

        is_admin = await sync_to_async(
            TelegramAdmin.objects.filter(chat_id=message.from_user.id).exists
        )()

        return is_admin
