from aiogram.fsm.state import State, StatesGroup


class ManageStates(StatesGroup):
    manage = State()


class AdminStates(StatesGroup):
    admin = State()
    add = State()
    remove = State()


class UploadStates(StatesGroup):
    upload = State()
    language = State()
    image = State()
    confirm = State()
    finish = State()
