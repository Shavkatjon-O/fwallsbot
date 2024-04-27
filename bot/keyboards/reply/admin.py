from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestUser
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class AdminKeyboard:
    admins = "📋 Список админов"
    add = "➕ Добавить"
    remove = "➖ Удалить"
    back = "🔙 Назад"

    @classmethod
    def get_keyboard(cls) -> ReplyKeyboardMarkup:
        buttons = [
            [KeyboardButton(text=cls.admins)],
            [KeyboardButton(text=cls.add)],
            [KeyboardButton(text=cls.remove)],
            [KeyboardButton(text=cls.back)],
        ]
        keyboard = ReplyKeyboardBuilder(markup=buttons)
        keyboard.adjust(1, 2, 1)

        return keyboard.as_markup(
            resize_keyboard=True,
        )


class AddAdminKeyboard:
    select = "📋 Выбрать админа"
    back = "🔙 Назад"

    @classmethod
    def get_keyboard(cls) -> ReplyKeyboardMarkup:
        buttons = [
            [
                KeyboardButton(
                    text=cls.select,
                    request_user=KeyboardButtonRequestUser(
                        request_id=1,
                        user_is_bot=False,
                    ),
                )
            ],
            [KeyboardButton(text=cls.back)],
        ]
        keyboard = ReplyKeyboardBuilder(markup=buttons)
        keyboard.adjust(1)

        return keyboard.as_markup(
            resize_keyboard=True,
        )


class RemoveAdminKeyboard:
    back = "🔙 Назад"

    @classmethod
    def get_keyboard(cls) -> ReplyKeyboardMarkup:
        buttons = [
            [KeyboardButton(text=cls.back)],
        ]
        keyboard = ReplyKeyboardBuilder(markup=buttons)
        keyboard.adjust(1)

        return keyboard.as_markup(
            resize_keyboard=True,
        )
