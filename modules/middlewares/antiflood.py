# antiflood.py

from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled
from aiogram.types import ParseMode


class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, dispatcher, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
        self.dispatcher = dispatcher
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler:
            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"
        try:
            await self.dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            await self.message_throttled(message, t)
            raise CancelHandler()

    async def on_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        handler = current_handler.get()
        if handler:
            # Получаем настройки throttling из декоратора 
            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        
        try:
            await self.dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            await self.callback_query_throttled(callback_query, t)
            raise CancelHandler()
            
    async def callback_query_throttled(self, callback_query: types.CallbackQuery, throttled: Throttled):
        await callback_query.answer()
        await callback_query.message.reply("⚠️ *Вы сделали слишком много запросов! Подождите пару секунд и попробуйте снова!*", parse_mode=ParseMode.MARKDOWN)

    async def message_throttled(self, message: types.Message, throttled: Throttled):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler:
            key = getattr(handler, "throttling_key")
        else:
            key = f"{self.prefix}_message"
        await message.reply(f"⚠️ *Вы сделали слишком много запросов! Подождите пару секунд и попробуйте снова!*", parse_mode=ParseMode.MARKDOWN)


def rate_limit(limit: int, key=None):
    def decorator(func):
        setattr(func, "throttling_rate_limit", limit)
        if key:
            setattr(func, "throttling_key", key)
        return func

    return decorator