# db.py
import aiosqlite
import datetime

# Создание таблицы пользователей
async def create_table():
    async with aiosqlite.connect("users.db") as conn:
        await conn.execute("""CREATE TABLE IF NOT EXISTS users
                              (user_id INTEGER PRIMARY KEY, first_start TEXT)""")
        await conn.commit()

# Добавление нового пользователя
async def add_user(user_id, first_start):
    async with aiosqlite.connect("users.db") as conn:
        first_start_str = first_start.strftime('%Y-%m-%d %H:%M:%S')
        await conn.execute("INSERT INTO users (user_id, first_start) VALUES (?, ?)", (user_id, first_start_str))
        await conn.commit()

# Получение данных пользователя
async def get_user(user_id):
    async with aiosqlite.connect("users.db") as conn:
        async with conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,)) as cursor:
            user_data = await cursor.fetchone()
    if user_data:
        return {"user_id": user_data[0], "first_start": user_data[1]}
    return None

# Обновление данных пользователя
async def update_user_data(user_id, new_data):
    async with aiosqlite.connect("users.db") as conn:
        await conn.execute("UPDATE users SET first_start=? WHERE user_id=?", (new_data, user_id))
        await conn.commit()