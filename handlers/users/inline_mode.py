import random
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp, bot








@dp.inline_handler(text='1')
async def empty_quaery(quaery: types.InlineQuery):
    await quaery.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="1",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"1"

                ),
                thumb_url="https://klike.net/uploads/posts/2020-02/1581844900_1.jpg",
                description='Золото'
            )
        ],
        cache_time=5
    )


@dp.inline_handler(text='2')
async def empty_quaery(quaery: types.InlineQuery):
    await quaery.answer(
        results=[
            types.InlineQueryResultArticle(
                id="2",
                title="2",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"2"

                ),
                thumb_url="https://s0.rbk.ru/v6_top_pics/media/img/1/05/755892967328051.jpg",
                description='Серебро'
            )

        ],
        cache_time=5
    )

@dp.inline_handler()
async def empty_quaery(quaery: types.InlineQuery):
    keybord = types.InlineKeyboardMarkup()
    swithc_button = types.InlineKeyboardButton(text="Поделится", switch_inline_query="🔮How it's true?")
    keybord.add(swithc_button)
    # if quaery.from_user.id == 615604689 or 658597670:
    #     text = "Я пидорас на 100%"
    # else:
    #     text = f"Я думаю это правда на {random.randint(0,100)}%"
    await quaery.answer(
        results=[
            types.InlineQueryResultArticle(
                id="work",
                title="🔮 How it's true?",
                input_message_content= types.InputTextMessageContent(
                     message_text=f"Я думаю это правда на {random.randint(0,100)}%"),
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=
                    [
                        [
                            InlineKeyboardButton(text="Поделится!🔮",
                                                 switch_inline_query="")
                        ]
                    ]
                ),
                thumb_url="https://st2.depositphotos.com/1653909/8228/i/600/depositphotos_82284502-stock-photo-magician-hands-with-magic-wand.jpg",
                description="Узнать на сколько это правда"

            )

        ],
        cache_time= 5
    )