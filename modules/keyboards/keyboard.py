from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

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

