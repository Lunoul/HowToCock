from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

async def profile_info(call):
    # get user information from the callback query
    user = call.from_user
    user_id = user.id
    user_name = user.username
    user_language = user.language_code

    # create profile information message
    profile_message = (
        f"👤 *Информация о профиле:*\n\n"
        f"*ID:* `{user_id}`\n"
        f"*Юзернейм:* `{user_name}`\n"
        f"*Язык:* `{user_language}`\n\n"
        f"*Тут должен быть донат* /donate\n\n"
    )

    await call.message.edit_text(profile_message, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard_profile())


def keyboard_profile():
	# create return to main menu button
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(types.InlineKeyboardButton(text="🔙 К выбору стран", callback_data="start"))
	return keyboard
