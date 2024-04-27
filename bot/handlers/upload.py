from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from aiogram.types import Message, ContentType
from aiogram.fsm.context import FSMContext

from asgiref.sync import sync_to_async

from bot.keyboards.reply.upload import (
    UploadKeyboard,
    FinishKeyboard,
    ConfirmKeyboard,
    CancelKeyboard,
)
from bot.keyboards.reply.language import LanguageKeyboard

from bot.filters.admin import AdminFilter
from bot.handlers.manage import command_manage
from bot.states.admin import UploadStates
from bot.models import Image, ImageGroup


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
    await state.set_state(UploadStates.finish)


@router.message(UploadStates.confirm, F.text == ConfirmKeyboard.replace)
async def replace_image(message: Message, state: FSMContext) -> None:
    text = "🔄 Пришлите новое изображение для замены"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(UploadStates.image)


@router.message(UploadStates.finish, F.text == FinishKeyboard.add)
async def add_image(message: Message, state: FSMContext) -> None:
    text = "📤 Пришлите мне изображение, которое хотите загрузить"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(UploadStates.image)


@router.message(UploadStates.finish, F.text == FinishKeyboard.upload)
async def upload_all_images(message: Message, state: FSMContext) -> None:
    text = "🌐 Выберите язык, для которого загружаются изображения"
    await message.answer(text=text, reply_markup=LanguageKeyboard.get_keyboard())
    await state.set_state(UploadStates.language)


@router.message(
    UploadStates.language,
    F.text.in_([LanguageKeyboard.russian, LanguageKeyboard.uzbek]),
)
async def finish_upload_image(message: Message, state: FSMContext) -> None:
    language = "ru" if message.text == LanguageKeyboard.russian else "uz"

    data = await state.get_data()
    media_group = data.get("media_group", [])

    images = []
    image_group = await sync_to_async(ImageGroup.objects.create)(language=language)

    for _message in media_group:
        file_id = (
            _message.photo[-1].file_id if _message.photo else _message.document.file_id
        )
        content_type = _message.content_type

        image = Image(
            image_group=image_group, file_id=file_id, content_type=content_type
        )
        images.append(image)

    await sync_to_async(Image.objects.bulk_create)(images)

    bot_info = await message.bot.get_me()

    invite_link = "https://t.me/{}/?start={}"
    invite_link = invite_link.format(bot_info.username, image_group.id)

    await message.answer(text=invite_link)

    text = "✅ Изображения успешно загружены."
    await message.answer(text=text, reply_markup=UploadKeyboard.get_keyboard())

    await state.clear()
    await state.set_state(UploadStates.upload)
