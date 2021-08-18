from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from filters import IsPrivate
import json

@dp.message_handler(Command("get_update"))
async def bot_echo(message: types.Message):
    json_message = json.loads(str(message))
    json_message = f"<pre>{json.dumps(json_message, indent = 1, ensure_ascii = False)}</pre>"
    await message.answer(json_message)


@dp.message_handler(IsPrivate())
async def bot_echo(message: types.Message):
    await message.reply(text=f"Ехо {message.text}")


