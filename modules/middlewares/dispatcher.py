import logging
import sys
from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import ValidationError

from config import TOKEN, MODE

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

if MODE == 'prod':
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
        )
elif MODE == 'dev':
    logging.basicConfig(level=logging.DEBUG)
