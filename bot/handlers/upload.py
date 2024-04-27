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


@router.message(UploadStates.upload, F.text == UploadKeyboard.upload)
async def upload_image(message: Message, state: FSMContext) -> None:
    text = "📤 Пришлите мне изображение, которое хотите загрузить."
    await message.answer(text=text, reply_markup=CancelKeyboard.get_keyboard())
    await state.set_state(UploadStates.image)


@router.message(UploadStates.image, F.text == CancelKeyboard.cancel)
async def cancel_upload(message: Message, state: FSMContext) -> None:
    await state.clear()
    await command_upload(message, state)
