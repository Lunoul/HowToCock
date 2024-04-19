import os
# модули методов и стран
# from handlers import methods_chosen, countries_chosen
# Модули функционала
import modules.database.db as db
import modules.handlers.admin as admin
from modules.utils.handlers import methods_chosen, countries_chosen
import modules.keyboards.profile as profile
import modules.keyboards.startbuttons as startbuttons
from modules.keyboards.profile import profile_info
from modules.keyboards.startchannels import startchannels, channel
from modules.middlewares.antiflood import ThrottlingMiddleware, rate_limit
from modules.middlewares.states import Form
from modules.middlewares.dispatcher import dp, storage, bot
from config import TOKEN, admin_id


# aiogram
import aiogram.utils.markdown as fmt
import aiogram.types
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor

dp.middleware.setup(ThrottlingMiddleware(dispatcher=dp))

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота")
    ])

@rate_limit(3, "start")
@dp.message_handler(commands=['start'], state='*')
async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    username = message.from_user.username
    user_id = message.from_user.id
    if not username:
        username = message.from_user.first_name # Если нет юзернейма, то берем имя
    db.add_user(user_id, username)

    subscribed = db.get_subscribed(user_id)
    if subscribed:
        await message.answer("Откройте для себя бесконечные возможности для экспериментов и поиска нужной информации!\n\n*Выберите нужную вам страну для поиска:* ", reply_markup=startbuttons.startbuttos(), parse_mode=ParseMode.MARKDOWN)
        await state.finish()
    else:
        await startchannels(message)

@dp.callback_query_handler(text="start", state='*')
async def start_over(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await cmd_start(call.message, state)

@dp.callback_query_handler(text='checksubs')  # Обработчик для проверки подписки
async def checker(call: types.CallbackQuery):
    await call.answer()
    # проверка подписки
    bot_info = await bot.get_me()
    bot_username = bot_info.username
    chat_member = await bot.get_chat_member(chat_id=channel, user_id=call.from_user.id)

    if chat_member.status != 'left': # Если пользователь не покинул канал
        db.set_subscribed(call.from_user.id, 1) # Устанавливаем подписку в базе
        # Удалить старое сообщение и Сделать переход в старотовое меню
        await call.message.delete()
        await call.message.answer("Откройте для себя бесконечные возможности для экспериментов и поиска нужной информации!\n\n*Выберите нужную вам страну для поиска:* ", reply_markup=startbuttons.startbuttos(), parse_mode=ParseMode.MARKDOWN)

    else:
        await call.message.answer("Вы не подписались на канал") # Если пользователь покинул канал
        db.set_subscribed(call.from_user.id, 0)

@dp.message_handler(commands=['admin'], user_id=admin_id)
async def cmd_admin(message: types.Message):
    await admin.admin_info(message)

@rate_limit(3, "profile_info")
@dp.callback_query_handler(text="profile") # Обработчик для профиля
async def profile(call: types.CallbackQuery): 
    await profile_info(call)

@rate_limit(3, "methods_chosen")
@dp.callback_query_handler(text="startmethods") # Обработчик для стартового меню
async def startmethods(call: types.CallbackQuery, state: FSMContext): 
    state = FSMContext(storage, call.from_user.id, None) # Создаем объект состояния
    await methods_chosen(call, state) # Переходим в состояние выбора метода

@rate_limit(3, "country_chosen")
@dp.callback_query_handler(text="startcountries") # Обработчик для стартового меню
async def startcountries(call: types.CallbackQuery): 
    state = FSMContext(storage, call.from_user.id, None) # Создаем объект состояния
    await countries_chosen(call, state) # Переходим в состояние выбора метода

@dp.callback_query_handler(Text(startswith="search_"), state=Form.country)
async def searcher(call: types.CallbackQuery, state: FSMContext):
    await call.answer() 
    method, country = call.data.split("_")[1:3]

    data_dir = os.path.join(os.path.dirname(__file__), "data") # Путь к папке data
    country_dir = os.path.join(data_dir, country) # Путь к папке страны
    file_path = os.path.join(country_dir, f"{method}.txt")
    with open(file_path, "r", encoding="utf-8") as f: # Читаем файл
        text = f.read()
    
    # Устанавливаем максимальную длину сообщения для разбиения текста
    max_message_length = 4096  # Подставьте свою желаемую максимальную длину сообщения

    # Разбиваем текст на сообщения с максимальной длиной
    messages = [text[i:i+max_message_length] for i in range(0, len(text), max_message_length)]

    for i, message_text in enumerate(messages):
        # Добавляем номер к сообщению (если нужно)
        #message_text = f"{i+1} часть.\n {message_text}"
        await call.message.answer(fmt.text(message_text), disable_web_page_preview=True)

    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=set_default_commands)