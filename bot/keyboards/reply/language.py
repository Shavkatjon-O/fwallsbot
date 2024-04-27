from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton


class LanguageKeyboard:
    russian = "🇷🇺 Русский"
    uzbek = "🇺🇿 O'zbek"

    @classmethod
    def get_keyboard(cls) -> ReplyKeyboardMarkup:
        buttons = [
            [KeyboardButton(text=cls.russian)],
            [KeyboardButton(text=cls.uzbek)],
        ]
        keyboard = ReplyKeyboardBuilder(markup=buttons)
        keyboard.adjust(2)

        return keyboard.as_markup(
            resize_keyboard=True,
        )
