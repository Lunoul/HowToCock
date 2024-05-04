from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import CHANNEL_LINK

# Клавиатура для выбора действия
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🗂 Методы", callback_data="methods"),
            InlineKeyboardButton(text="👤 Профиль", callback_data="profile")
        ]
    ]
)

# Клавиатура для выбора метода
methods_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="☎️ Phone number", callback_data="phone_number")],
        [InlineKeyboardButton(text="👾 Username", callback_data="username")],
        [InlineKeyboardButton(text="👤 Fullname", callback_data="fullname")],
        [InlineKeyboardButton(text="🚗 CarNumber", callback_data="car_number")],
        [InlineKeyboardButton(text="👽 FaceScan", callback_data="face_scan")]
    ], row_width=1
)

back_to_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="back_to_menu")]
    ]
)

subscribe_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="❌ Подписаться на канал", url=CHANNEL_LINK)]
    ]
)