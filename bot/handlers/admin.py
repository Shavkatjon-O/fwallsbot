from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from asgiref.sync import sync_to_async

from bot.handlers.manage import command_manage
from bot.models import TelegramAdmin

from bot.states.admin import AdminStates
from bot.keyboards.reply.admin import (
    AdminKeyboard,
    RemoveAdminKeyboard,
    AddAdminKeyboard,
)
from bot.filters.admin import AdminFilter


router = Router(name="admin")


@router.message(Command("admin"), AdminFilter())
async def command_admin(message: Message, state: FSMContext) -> None:
    text = "💎 Выберите действие"
    await message.answer(text=text, reply_markup=AdminKeyboard.get_keyboard())
    await state.set_state(AdminStates.admin)


@router.message(AdminStates.admin, F.text == AdminKeyboard.back)
async def back_to_manage(message: Message, state: FSMContext) -> None:
    await state.clear()
    await command_manage(message, state)


@router.message(AdminStates.admin, F.text == AdminKeyboard.add)
async def add_admin(message: Message, state: FSMContext) -> None:
    text = "📋 Выберите админа для добавления"
    await message.answer(text=text, reply_markup=AddAdminKeyboard.get_keyboard())
    await state.set_state(AdminStates.add)


@router.message(AdminStates.admin, F.text == AdminKeyboard.remove)
async def remove_admin(message: Message, state: FSMContext) -> None:
    text = "📋 Выберите админа для удаления"
    keyboard = await RemoveAdminKeyboard.aget_keyboard()
    await message.answer(text=text, reply_markup=keyboard)
    await state.set_state(AdminStates.remove)


@router.message(AdminStates.remove, F.text == RemoveAdminKeyboard.back)
async def back_admin_remove(message: Message, state: FSMContext) -> None:
    await state.clear()
    await command_admin(message, state)


@router.message(AdminStates.add, F.text == AddAdminKeyboard.back)
async def back_admin_add(message: Message, state: FSMContext) -> None:
    await state.clear()
    await command_admin(message, state)


@router.message(AdminStates.add)
async def select_admin_to_add(message: Message, state: FSMContext) -> None:
    shared_user_id = message.user_shared.user_id

    if message.from_user.id == shared_user_id:
        await message.answer(text="🚫 Нельзя добавить самого себя")
        return

    try:
        chat_info = await message.bot.get_chat(shared_user_id)
    except Exception:
        await message.answer(text="🚫 Не удалось получить информацию о пользователе")
        return

    admin, created = await sync_to_async(TelegramAdmin.objects.get_or_create)(
        chat_id=chat_info.id,
        username=chat_info.username,
        first_name=chat_info.first_name,
        last_name=chat_info.last_name,
    )

    text = "✅ Админ добавлен" if created else "🚫 Админ уже добавлен"
    await message.answer(text=text, reply_markup=AdminKeyboard.get_keyboard())

    await state.clear()
    await state.set_state(AdminStates.admin)
