from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestUser
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class UploadKeyboard:
    upload = "📥 Загрузить изображение"
    back = "🔙 Назад"

    @classmethod
    def get_keyboard(cls) -> ReplyKeyboardMarkup:
        buttons = [
            [KeyboardButton(text=cls.upload)],
            [KeyboardButton(text=cls.back)],
        ]
        keyboard = ReplyKeyboardBuilder(markup=buttons)
        keyboard.adjust(1)

        return keyboard.as_markup(
            resize_keyboard=True,
        )


class FinishKeyboard:
    add = "➕ Добавить"
    upload = "📥 Загрузить все"
    cancel = "❌ Отменить все"

    @classmethod
    def get_keyboard(cls) -> ReplyKeyboardMarkup:
        buttons = [
            [KeyboardButton(text=cls.add)],
            [KeyboardButton(text=cls.upload)],
            [KeyboardButton(text=cls.cancel)],
        ]
        keyboard = ReplyKeyboardBuilder(markup=buttons)
        keyboard.adjust(1, 2)

        return keyboard.as_markup(
            resize_keyboard=True,
        )


class ConfirmKeyboard:
    confirm = "✅ Подтвердить"
    replace = "🔄 Заменить"

    @classmethod
    def get_keyboard(cls) -> ReplyKeyboardMarkup:
        buttons = [
            [KeyboardButton(text=cls.confirm)],
            [KeyboardButton(text=cls.replace)],
        ]
        keyboard = ReplyKeyboardBuilder(markup=buttons)
        keyboard.adjust(2)

        return keyboard.as_markup(
            resize_keyboard=True,
        )


class CancelKeyboard:
    cancel = "❌ Отменить"

    @classmethod
    def get_keyboard(cls) -> ReplyKeyboardMarkup:
        buttons = [
            [KeyboardButton(text=cls.cancel)],
        ]
        keyboard = ReplyKeyboardBuilder(markup=buttons)
        keyboard.adjust(1)

        return keyboard.as_markup(
            resize_keyboard=True,
        )
