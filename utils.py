from aiogram import Bot
import os

# Проверка подписки на канал
async def check_subscription(bot: Bot, user_id, channel_id):
    member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
    return member.status in ["creator", "administrator", "member"]

# Чтение содержимого файла
def read_file(file_name):
    folder_path = os.path.join(os.path.dirname(__file__), "data")
    file_path = os.path.join(folder_path, file_name + ".txt")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    else:
        return f"Файл {file_name}.txt не найден"

# Разбиение длинного текста на сообщения
MAX_MESSAGE_LENGTH = 4096

def split_long_text(text):
    if len(text) <= MAX_MESSAGE_LENGTH:
        return [text]
    else:
        chunks = []
        while text:
            chunk = text[:MAX_MESSAGE_LENGTH]
            chunks.append(chunk)
            text = text[MAX_MESSAGE_LENGTH:]
        return chunks