from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class ManageKeyboard:
    admin = "💎 Админы"
    upload = "🖼️ Обои"

    @classmethod
    def get_keyboard(cls) -> ReplyKeyboardMarkup:
        buttons = [
            [KeyboardButton(text=cls.admin)],
            [KeyboardButton(text=cls.upload)],
        ]
        keyboard = ReplyKeyboardBuilder(markup=buttons)
        keyboard.adjust(2)

        return keyboard.as_markup(
            resize_keyboard=True,
        )


def get_manage_buttons() -> ReplyKeyboardMarkup:
    from bot.handlers.admin import command_admin
    from bot.handlers.upload import command_upload

    buttons = {
        ManageKeyboard.admin: command_admin,
        ManageKeyboard.upload: command_upload,
    }
    return buttons
