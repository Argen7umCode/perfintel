from aiogram.fsm.state import State, StatesGroup


class AddRecord(StatesGroup):
    category = State()
    amount = State()