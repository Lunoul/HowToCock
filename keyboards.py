# keyboards.py
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура для выбора действия
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Профиль", callback_data="profile")],
        [InlineKeyboardButton(text="Методы", callback_data="methods")]
    ]
)

# Клавиатура для выбора метода
methods_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Username", callback_data="username")],
        [InlineKeyboardButton(text="Phone number", callback_data="phone_number")]
    ]
)