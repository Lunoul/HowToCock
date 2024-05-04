import logging
import asyncio
from aiogram import Dispatcher, executor, types, Bot
from aiogram.dispatcher import FSMContext

from config import BOT_TOKEN, CHANNEL_ID
from dispatcher import dp, bot
from db import create_table, add_user, get_user
from handlers import handlers
from states import UserState
from keyboards import start_keyboard, subscribe_keyboard
from utils import check_subscription

# Настройка логгирования
logging.basicConfig(level=logging.INFO)

# Обработчик команды /start
@dp.message_handler(commands=['start'], state='*')
async def start_command(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    is_subscribed = await check_subscription(bot, user_id, CHANNEL_ID)

    if not is_subscribed:
        await message.answer("*🖐 Вы не подписаны на наш канал. Подпишитесь, чтобы продолжить:*", reply_markup=subscribe_keyboard)
        await state.set_state(UserState.waiting_for_channel_subscription)
        return

    if not await get_user(user_id):
        await add_user(user_id, message.date)

    await message.answer("*Откройте для себя бесконечные возможности для экспериментов и поиска нужной информации!*", reply_markup=start_keyboard)
    await state.set_state(UserState.idle)

# Обработчик выбора действия
@dp.callback_query_handler(state=UserState.idle)
async def process_action(callback: types.CallbackQuery, state: FSMContext):
    action = callback.data
    handler = handlers.get(action)
    if handler:
        await handler(callback)

# Обработчик проверки подписки на канал
@dp.callback_query_handler(state=UserState.waiting_for_channel_subscription)
async def check_channel_subscription(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    is_subscribed = await check_subscription(bot, user_id, CHANNEL_ID)

    if is_subscribed:
        await start_command(callback.message, state)
    else:
        await callback.message.edit_reply_markup(subscribe_keyboard)
        await callback.answer("*Вы не подписаны на наш канал. Подпишитесь, чтобы продолжить.*", show_alert=True)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(create_table())
    executor.start_polling(dp, skip_updates=True)