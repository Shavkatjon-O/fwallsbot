from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.handlers.manage import command_manage

from bot.states.admin import AdminStates
from bot.keyboards.reply.admin import AdminKeyboard
from bot.filters.admin import AdminFilter


router = Router(name="admin")


@router.message(Command("admin"), AdminFilter())
async def command_admin(message: Message, state: FSMContext) -> None:
    text = "💎 Админы"
    await message.answer(text=text, reply_markup=AdminKeyboard.get_keyboard())
    await state.set_state(AdminStates.admin)


@router.message(AdminStates.admin, F.text == AdminKeyboard.back)
async def back_to_manage(message: Message, state: FSMContext) -> None:
    await state.clear()
    await command_manage(message, state)
