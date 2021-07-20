from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

add_to_chanel = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Добавить в каналы 📝", callback_data="add_to_chanels")
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="do_not_chanels")
        ]
    ]
)