from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data import admins
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}. Бот запущен, и готов к работе!')
    await message.answer_sticker(r"CAACAgIAAxkBAAEBOo9fPkNBsWHTZkjMDx-swASvV-Cj-AACIgADTlzSKWF0vv5zFvwUGwQ")
    await bot.send_message(chat_id=454793780, text=f"User {message.from_user.get_mention(as_html=True)} is join to bot")

