from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router(name="upload")


@router.message(Command("upload"))
async def command_upload(message: Message) -> None:
    pass
