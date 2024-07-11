# bot version: 1.3

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config as cfg


bot = Bot(cfg.7294993191:AAEFCphfC1PraUbSkD8IyWvTEg6qGGyvAtQ, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
