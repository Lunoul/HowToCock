import aiogram
from aiogram import types
from dispatcher import dp, bot
from db import get_user
from keyboards import methods_keyboard, back_to_menu_keyboard, start_keyboard
from utils import read_file, split_long_text
from states import UserState
import datetime

async def handle_back_to_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("*Откройте для себя бесконечные возможности для экспериментов и поиска нужной информации!*", reply_markup=start_keyboard)
async def handle_profile(callback: types.CallbackQuery):
    user_data = await get_user(callback.from_user.id)
    first_start = datetime.datetime.strptime(user_data['first_start'], '%Y-%m-%d')
    profile_text = f"👤 *Информация о профиле:*\n*Ваш ID:* {user_data['user_id']}\n*Дата первого запуска:* {first_start.strftime('%Y-%m-%d')}"
    await callback.message.edit_text(profile_text, reply_markup=back_to_menu_keyboard)

async def handle_methods(callback: types.CallbackQuery):
    await callback.message.edit_text("⬇️ *Выберите нужный вам метод поиска:*", reply_markup=methods_keyboard)

async def handle_method(callback: types.CallbackQuery):
    method = callback.data
    file_content = read_file(method)
    text_chunks = split_long_text(file_content)

    # Удалить сообщение "Выберите нужный вам метод поиска:"
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    for i, chunk in enumerate(text_chunks):
        try:
            # Если это последний кусок текста, добавьте кнопку "Назад в меню"
            if i == len(text_chunks) - 1:
                await bot.send_message(callback.message.chat.id, chunk, reply_markup=back_to_menu_keyboard, disable_web_page_preview=True, parse_mode="HTML")
            else:
                await bot.send_message(callback.message.chat.id, chunk, disable_web_page_preview=True, parse_mode="HTML")
        except aiogram.utils.exceptions.MessageTextIsEmpty:
            await callback.message.edit_text("Извините, произошла ошибка при отображении содержимого файла. Пожалуйста, попробуйте еще раз позже.")
            break

handlers = {
    "profile": handle_profile,
    "methods": handle_methods,
    "back_to_menu": handle_back_to_menu,
    "username": handle_method,
    "phone_number": handle_method,
    "fullname": handle_method,
    "car_number": handle_method,
    "face_scan": handle_method,
}

__all__ = ["handlers"]  # Экспорт словаря handlers

@dp.callback_query_handler(state=UserState.idle)
async def process_action(callback: types.CallbackQuery):
    action = callback.data
    handler = handlers.get(action)
    if handler:
        await handler(callback)