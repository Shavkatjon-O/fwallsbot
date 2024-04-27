from aiogram import Router, F
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
from bot.handlers.manage import command_manage
from bot.states.admin import UploadStates


router = Router(name="upload")


@router.message(Command("upload"), AdminFilter())
async def command_upload(message: Message, state: FSMContext) -> None:
    text = "🖼️ Выберите действие"
    await message.answer(text=text, reply_markup=UploadKeyboard.get_keyboard())
    await state.set_state(UploadStates.upload)


@router.message(UploadStates.upload, F.text == UploadKeyboard.back)
async def back_to_manage(message: Message, state: FSMContext) -> None:
    await state.clear()
    await command_manage(message, state)
