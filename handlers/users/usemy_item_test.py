from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

# from keyboards.inline.callback_datas import item_callback, item_rating
from loader import dp, bot

golden_item = {
    "photo": "https://klike.net/uploads/posts/2020-02/1581844900_1.jpg",
    "name": "Золото",
    "id": 1,
    "rating": 0
}
silver_item = {
    "photo": "https://s0.rbk.ru/v6_top_pics/media/img/1/05/755892967328051.jpg",
    "name": "Серебро",
    "id": 2,
    "rating": 0
}

item_keyboard = InlineKeyboardMarkup()
item_callback = CallbackData("buy", "item_id")
item_rating = CallbackData("rating", "r", "item_id")

def generation(item):

    global item_keyboard
    item_keyboard = InlineKeyboardMarkup(row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"Купить товар",
                                         callback_data= item_callback.new(item_id =item['id']))
                ],
                [
                    InlineKeyboardButton(text="👍",
                                         callback_data= item_rating.new(r = "True", item_id = f"{item['id']}")),
                    InlineKeyboardButton(text="👎",
                                         callback_data= item_rating.new(r = "False", item_id = f"{item['id']}"))

                ],
                [
                    InlineKeyboardButton(text="Поделиться с другом",
                                         switch_inline_query=f"{item['id']}"
                                         ),
                ]
            ])

@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await bot.send_message(chat_id=454793780, text=f"User {message.from_user.get_mention(as_html=True)} turn on /item")
    generation(golden_item)
    await bot.send_photo(photo=golden_item.get('photo'),
                         chat_id=message.from_user.id,
                         caption=f"{golden_item.get('name')}",
                         reply_markup=item_keyboard)
    generation(silver_item)
    await bot.send_photo(photo=silver_item.get('photo'),
                         chat_id=message.from_user.id,
                         caption=f"{silver_item.get('name')}",
                         reply_markup=item_keyboard)


@dp.callback_query_handler(item_callback.filter(item_id='1'))
async def buy_item(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    #await call.message.edit_reply_markup()
    await bot.edit_message_caption(chat_id=call.from_user.id,message_id=call.message.message_id,
                                   caption=f"Покупай товар номер {golden_item['id']}", reply_markup=None)


@dp.callback_query_handler(item_callback.filter(item_id='2'))
async def buy_item(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    #await call.message.edit_reply_markup()
    await bot.edit_message_caption(chat_id=call.from_user.id, message_id=call.message.message_id,
                                   caption=f"Покупай товар номер {silver_item['id']}", reply_markup=None)



@dp.callback_query_handler(item_rating.filter(r="True"))
async def items(call: types.CallbackQuery):
    await call.answer("Тебе понравился этот товар", cache_time=2)

@dp.callback_query_handler(item_rating.filter(r="False"))
async def items(call: types.CallbackQuery):
    await call.answer("Тебе не понравился этот товар", cache_time=2)
