from aiogram import types
import modules.database.db

async def admin_info(message: types.Message): # Функция для вывода информации о пользователях

  users_count = db.get_users_count()

  response = f"Пользователей бота: {users_count}"

  await message.answer(response)

