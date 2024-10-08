from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command


hello_world_router = Router()


@hello_world_router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


# @hello_world_router.message()
# async def message_handler(msg: Message):
#     await msg.answer(f"Твой ID: {msg.from_user.id}")