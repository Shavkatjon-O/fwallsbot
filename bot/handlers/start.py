from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router(name="start")


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer(text="Hello, I am bot !")
