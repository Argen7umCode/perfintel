import datetime
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

from states import AddRecord
from utils.category import get_user_categories
from utils.record import save_user_record


add_record_router = Router()


@add_record_router.message(Command("add_record"))
async def command_add_record(message: Message, state: FSMContext) -> None:
    categories = await get_user_categories(message.from_user.id)
    await state.set_state(AddRecord.category)
    await message.answer(
        "Введи категорию дохода или расхода: \n" + '\n'.join(str(i) + '. ' + category for i, category in enumerate(categories, 1)),
        reply_markup=ReplyKeyboardRemove(),
    )

@add_record_router.message(AddRecord.category)
async def get_category(msg: Message, state: FSMContext) -> None:
    await state.update_data(category=msg.text)
    await state.set_state(AddRecord.amount)

    await msg.answer(
        "Введи сумму дохода или расхода",
        reply_markup=ReplyKeyboardRemove(),
    )

@add_record_router.message(AddRecord.amount)
async def get_amount(msg: Message, state: FSMContext) -> None:
    await state.update_data(amount=msg.text)
    await state.set_state(None)

    data = await state.get_data()
    record = {
        "category": data["category"],
        "amount": data["amount"],
        "user_id": msg.from_user.id,
        "date": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
    }
    await save_user_record(msg.from_user.id, record)
    await msg.answer(
        f"Категория: {data['category']}\n"
        f"Сумма: {data['amount']}"
    )