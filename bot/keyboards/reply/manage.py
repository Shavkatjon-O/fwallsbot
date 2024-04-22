from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.handlers.admin import command_admin


class ManageKeyboard:
    ADMIN = "Администраторы 💎"

    @classmethod
    def get_keyboard(cls) -> ReplyKeyboardMarkup:
        buttons = [
            [KeyboardButton(text=cls.ADMIN)],
        ]
        keyboard = ReplyKeyboardBuilder(markup=buttons)
        keyboard.adjust(1)

        return keyboard.as_markup(
            resize_keyboard=True,
        )


def get_manage_buttons() -> ReplyKeyboardMarkup:
    """Return manage buttons."""

    buttons = {
        ManageKeyboard.ADMIN: command_admin,
    }
    return buttons
