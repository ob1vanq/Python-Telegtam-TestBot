from aiogram.dispatcher.filters.state import StatesGroup, State


class SugPost(StatesGroup):
    EnterMessage = State()
    Confirm = State()
