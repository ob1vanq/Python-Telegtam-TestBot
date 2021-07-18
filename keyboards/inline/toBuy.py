from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_item

BuyMarkup = InlineKeyboardMarkup(
    row_width= 1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💵 Купить товар",callback_data='buy')
        ],
        [
            InlineKeyboardButton(text="📢 Поделиться",switch_inline_query="Поделиться")
        ],
        [
            InlineKeyboardButton(text="Отмена",callback_data='cancel')
        ]
    ]
)

ChoseItem = InlineKeyboardMarkup(
    row_width= 2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Яблоко", callback_data=buy_item.new(item = 'apple')),
            InlineKeyboardButton(text="Груша",callback_data=buy_item.new(item = 'pear')),
        ],
        [
            InlineKeyboardButton(text="Отмена",callback_data='cancel')
        ]
    ]
)