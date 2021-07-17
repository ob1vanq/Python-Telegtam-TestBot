from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from filters import IsPrivate
import json

@dp.message_handler(Command("get_update"))
async def bot_echo(message: types.Message):
    await message.answer(f"<pre>{message}</pre>")

@dp.message_handler(IsPrivate())
async def bot_echo(message: types.Message):
    await message.answer(text=message.text)
    from .help import bot_help
    await bot_help(message)


