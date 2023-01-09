from config import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
