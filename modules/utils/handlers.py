from modules.middlewares.states import Form
from modules.middlewares.dispatcher import dp
from modules.keyboards.keyboard import *

from aiogram import types
from aiogram.types import ParseMode
from aiogram.dispatcher import FSMContext


async def methods_chosen(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Form.method)  # Устанавливаем состояние Form.method
    await call.message.edit_text("⬇️ *Выберите нужный вам метод поиска:*", reply_markup=get_methods_keyboard(), parse_mode=ParseMode.MARKDOWN) # Меняем сообщение и клавиатуру
@dp.callback_query_handler(text="PhoneNumber")
async def choose_telnumber(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.update_data(method="PhoneNumber")

@dp.callback_query_handler(text="FullName")
async def choose_fullname(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.update_data(method="FullName")

@dp.callback_query_handler(text="CarNumber")
async def choose_carnumber(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.update_data(method="CarNumber")

@dp.callback_query_handler(text="NickName")
async def choose_nickname(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.update_data(method="NickName")

@dp.callback_query_handler(text="FaceScan")
async def choose_facescan(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.update_data(method="FaceScan")