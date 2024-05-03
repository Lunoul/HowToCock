# keyboards.py
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import CHANNEL_LINK

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

back_to_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_to_menu")]
    ]
)

subscribe_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="❌ Подписаться на канал", url=CHANNEL_LINK)]
    ]
)