from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class ManageKeyboard:
    admin = "Админы 💎"

    @classmethod
    def get_keyboard(cls) -> ReplyKeyboardMarkup:
        buttons = [
            [KeyboardButton(text=cls.admin)],
        ]
        keyboard = ReplyKeyboardBuilder(markup=buttons)
        keyboard.adjust(1)

        return keyboard.as_markup(
            resize_keyboard=True,
        )


def get_manage_buttons() -> ReplyKeyboardMarkup:
    from bot.handlers.admin import command_admin

    buttons = {
        ManageKeyboard.admin: command_admin,
    }
    return buttons
