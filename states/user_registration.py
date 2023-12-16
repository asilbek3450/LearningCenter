from aiogram.dispatcher.filters.state import StatesGroup, State


class UserRegistration(StatesGroup):
    course = State()
    name = State()
    phone = State()
