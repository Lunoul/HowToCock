from modules.middlewares.states import Form
from modules.middlewares.dispatcher import dp
from modules.keyboards.keyboard import *

from aiogram import types
from aiogram.types import ParseMode
from aiogram.dispatcher import FSMContext


async def countries_chosen(call: types.CallbackQuery, state: FSMContext):
   data = await state.get_data()
   if "method" not in data:
      await call.answer("Выберите метод поиска сначала.", show_alert=True)
      return
   method = data["method"]
   await call.message.edit_text("⬇️ *Выберите нужный вам метод поиска:*", reply_markup=get_countries_keyboard(method), parse_mode=ParseMode.MARKDOWN)
   await Form.country.set()

async def methods_chosen(call: types.CallbackQuery, state: FSMContext): 
    await call.message.edit_text("⬇️ *Выберите нужный вам метод поиска:*", reply_markup=get_methods_keyboard(), parse_mode=ParseMode.MARKDOWN) # Меняем сообщение и клавиатуру

@dp.callback_query_handler(text="PhoneNumber")  
async def choose_telnumber(call, state: FSMContext):
   await state.update_data(method="PhoneNumber")
   await countries_chosen(call, state)

@dp.callback_query_handler(text="FullName")  
async def choose_fullname(call, state: FSMContext):
   await state.update_data(method="FullName")
   await countries_chosen(call, state)

@dp.callback_query_handler(text="CarNumber")  
async def choose_carnumber(call, state: FSMContext):
   await state.update_data(method="CarNumber")
   await countries_chosen(call, state)

@dp.callback_query_handler(text="NickName")
async def choose_nickname(call, state: FSMContext):
   await state.update_data(method="NickName")
   await countries_chosen(call, state)

@dp.callback_query_handler(text="FaceScan")
async def choose_facescan(call, state: FSMContext):
   await state.update_data(method="FaceScan")
   await countries_chosen(call, state)