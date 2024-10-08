from aiogram.fsm.state import State, StatesGroup


class Register(StatesGroup):
    name = State()
    categories = State()