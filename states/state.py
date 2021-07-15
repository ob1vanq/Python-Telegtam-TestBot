from aiogram.dispatcher.filters.state import StatesGroup, State


class udemy_test(StatesGroup):
    name_state = State()
    email_state = State()
    phone_number_state = State()

