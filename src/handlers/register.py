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

from states import Register
from utils.category import (
    get_categories_from_text, 
    save_user_categories, 
    get_user_categories
)

register_router = Router()


@register_router.message(Command("register"))
async def command_register(message: Message, state: FSMContext) -> None:
    await state.set_state(Register.name)
    await message.answer(
        "Введи свое имя",
        reply_markup=ReplyKeyboardRemove(),
    )
@register_router.message(Register.name)
async def get_name(msg: Message, state: FSMContext) -> None:
    await state.update_data(name=msg.text)
    await state.set_state(Register.categories)

    await msg.answer(
        "Теперь выбери категории, которые вы хотите сохранять.\n"\
        "Формат сообщения: категория1, категория2, категория3", 
        reply_markup=ReplyKeyboardRemove()
    )

@register_router.message(Register.categories)
async def get_categories(msg: Message, state: FSMContext) -> None:
    await state.update_data(categories=msg.text)
    await state.set_state(None)

    categories = get_categories_from_text(msg.text)
    await save_user_categories(user_id=msg.from_user.id, categories=categories)
    categories = await get_user_categories(msg.from_user.id)

    text = '\n'.join(str(i) + '. ' + category for i, category in enumerate(categories, 1))
    await msg.answer(
        "Спасибо за регистрацию!\n\n"\
        f"Ваши категории: \n{text}" 
    )