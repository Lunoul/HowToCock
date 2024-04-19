import aiogram.utils.markdown as fmt
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

channel = "@Testercnl"

async def startchannels(message):
    
    channel = "Testercnl"
    button_subscribe = InlineKeyboardButton(text='Подписаться', url=f'https://t.me/{channel}')
    button_check = InlineKeyboardButton(text='Проверить', callback_data='checksubs')
    
    keyboard = InlineKeyboardMarkup().add(button_subscribe).add(button_check)
    
    await message.answer("*Для использования бота необходимо подписаться на канал:*", 
                         reply_markup=keyboard, parse_mode="Markdown")