from aiogram import types
from dispatcher import dp
from db import get_user
from keyboards import methods_keyboard
from utils import read_file
from states import UserState
import datetime
async def handle_profile(callback: types.CallbackQuery):
    user_data = await get_user(callback.from_user.id)
    first_start = datetime.datetime.strptime(user_data['first_start'], '%Y-%m-%d %H:%M:%S')
    profile_text = f"Ваш ID: {user_data['user_id']}\nДата первого запуска: {first_start.strftime('%Y-%m-%d %H:%M:%S')}"
    await callback.message.edit_text(profile_text)

async def handle_methods(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите метод:", reply_markup=methods_keyboard)

async def handle_method(callback: types.CallbackQuery):
    method = callback.data
    file_content = read_file(method)
    await callback.message.edit_text(file_content)

handlers = {
    "profile": handle_profile,
    "methods": handle_methods,
    "username": handle_method,
    "phone_number": handle_method,
}

__all__ = ["handlers"]  # Экспорт словаря handlers

@dp.callback_query_handler(state=UserState.idle)
async def process_action(callback: types.CallbackQuery):
    action = callback.data
    handler = handlers.get(action)
    if handler:
        await handler(callback)