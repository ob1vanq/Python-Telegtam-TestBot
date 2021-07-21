from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from filters import IsPrivate

@dp.message_handler(Command("get_update"))
async def bot_echo(message: types.Message):
    await message.answer(f"<pre>{message}</pre>")

@dp.message_handler(IsPrivate())
async def bot_echo(message: types.Message):
    await message.reply(text=f"Ехо {message.text}")


