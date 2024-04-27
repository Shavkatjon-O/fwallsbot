from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from aiogram.fsm.context import FSMContext

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
    text = "📤 Пришлите мне изображение, которое хотите загрузить"
    await message.answer(text=text, reply_markup=CancelKeyboard.get_keyboard())
    await state.set_state(UploadStates.image)


@router.message(UploadStates.image, F.text == CancelKeyboard.cancel)
async def cancel_upload(message: Message, state: FSMContext) -> None:
    await state.clear()
    await command_upload(message, state)


@router.message(
    UploadStates.image,
    F.content_type.in_([ContentType.PHOTO, ContentType.DOCUMENT]),
)
async def save_image(message: Message, album: list[Message], state: FSMContext) -> None:
    text = "📤 Изображение успешно загружено"
    await message.answer(text=text, reply_markup=ConfirmKeyboard.get_keyboard())

    await state.update_data(album=album)
    await state.set_state(UploadStates.confirm)


@router.message(UploadStates.confirm, F.text == ConfirmKeyboard.confirm)
async def confirm_upload(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    media_group = data.get("media_group", [])
    album = data.get("album")

    media_group.extend(album)

    text = "📤 Изображение успешно загружено"
    await message.answer(text=text, reply_markup=FinishKeyboard.get_keyboard())

    await state.update_data(media_group=media_group)
    await state.set_state(UploadStates.upload)
