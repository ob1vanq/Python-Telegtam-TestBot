import random

from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.inline_mode_keyboard import keyboard, keyboard2
from loader import dp


@dp.message_handler(Command("is_true"))
async def is_true(message: types.Message):
    await message.answer(text="Воспользуйся кнопкой что бы посетить мир рандомайзера",
                         reply_markup=keyboard2)

@dp.inline_handler()
async def how_true_mode(query: types.InlineQuery):

    text = f"Я думаю это правда на <b>{random.randint(0,100)}%</b>"
    url = "https://st2.depositphotos.com/1653909/8228/i/600/depositphotos_82284502-stock-photo-magician-hands-with-magic-wand.jpg"

    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="how_true",
                title="🔮 How it's true?",
                input_message_content=types.InputTextMessageContent(
                    message_text=text
                ),
                reply_markup=keyboard,
                thumb_url=url,
                description="Узнать на сколько это правда"
          )
        ],
        cache_time=1
    )

