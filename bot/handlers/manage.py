from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards.reply.manage import ManageKeyboard, get_manage_buttons

from bot.states.admin import ManageStates
from bot.filters.admin import AdminFilter


router = Router(name="manage")


@router.message(Command("manage"), AdminFilter())
async def command_manage(message: Message, state: FSMContext) -> None:
    text = "🤖 Выберите действие:"
    await message.answer(text=text, reply_markup=ManageKeyboard.get_keyboard())
    await state.set_state(ManageStates.manage)


@router.message(ManageStates.manage, F.text == ManageKeyboard.ADMIN)
async def manage_buttons(message: Message, state: FSMContext) -> None:
    buttons = get_manage_buttons()
    await buttons[message.text](message, state)
