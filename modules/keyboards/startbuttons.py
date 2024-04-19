from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def startbuttos():
	keyboard = InlineKeyboardMarkup()
	keyboard.add(
		InlineKeyboardButton(text="🗂 Методы", callback_data="startmethods"),
		InlineKeyboardButton(text="👤 Профиль", callback_data="profile"),
	)
	return keyboard