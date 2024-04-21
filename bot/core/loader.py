from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode

from django.conf import settings

token = settings.TELEGRAM_BOT_TOKEN

bot = Bot(token=token, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
