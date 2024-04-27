from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards.reply.upload import (
    UploadKeyboard,
    FinishKeyboard,
    ConfirmKeyboard,
    CancelKeyboard,
)
from bot.filters.admin import AdminFilter


router = Router(name="upload")


@router.message(Command("upload"), AdminFilter())
async def command_upload(message: Message, state: FSMContext) -> None:
    pass
