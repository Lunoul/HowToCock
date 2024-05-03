from aiogram.dispatcher.filters.state import State, StatesGroup

class UserState(StatesGroup):
    waiting_for_channel_subscription = State()
    idle = State()