import random

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp, bot


@dp.message_handler(Command("is_true"))
async def is_true_message(message: types.Message):
    await bot.send_message(chat_id=454793780, text=f"User {message.from_user.get_mention(as_html=True)} use /is_true")
    await message.answer(f"Я думаю это правда на {random.randint(0,100)}%",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=
                             [
                                 [
                                     InlineKeyboardButton(text="Поделится! 🔮",
                                                          switch_inline_query="")
                                 ]
                             ]
                         ))




