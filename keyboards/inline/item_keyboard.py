
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import item_callback, item_rating


def generation(item):

    global item_keyboard
    item_keyboard = InlineKeyboardMarkup(row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"Купить {item['id']}",
                                         callback_data= item_callback.new(item_id =f"{item['id']}"))
                ],
                [
                    InlineKeyboardButton(text="👍",
                                         callback_data= item_rating.new(r = "True", item_id = f"{item['id']}")),
                    InlineKeyboardButton(text="👎",
                                         callback_data= item_rating.new(r = "False", item_id = f"{item['id']}"))

                ],
                [
                    InlineKeyboardButton(text="Поделится",
                                         switch_inline_query= f"{item['id']}"
                                         ),
                ]
            ])
