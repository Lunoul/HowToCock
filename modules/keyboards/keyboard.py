from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

def get_countries_keyboard(method):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
    InlineKeyboardButton(text="🌐 Общее", callback_data=f"search_{method}_World"))
    keyboard.add(
    InlineKeyboardButton(text="🇺🇦 Украина", callback_data=f"search_{method}_Ukraine"),
    InlineKeyboardButton(text="🇷🇺 Россия", callback_data=f"search_{method}_Russia"))
    keyboard.add(
    InlineKeyboardButton(text="🔙 Назад", callback_data="start"))
    return keyboard

def get_methods_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(text="☎️ поиска по номеру телефона", callback_data="PhoneNumber"),
        types.InlineKeyboardButton(text="👤 Поиск по имени", callback_data="FullName"), 
        types.InlineKeyboardButton(text="🚗 Поиск по авто", callback_data="CarNumber"),
        types.InlineKeyboardButton(text="📱 Поиск по никнейму", callback_data="NickName"),
        types.InlineKeyboardButton(text="👨 Поиск по фотографии", callback_data="FaceScan"),
        types.InlineKeyboardButton(text="🔙 Назад", callback_data="start"))
    return keyboard

