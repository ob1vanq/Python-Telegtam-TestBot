from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

ChekSub = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Проверить подписку 🔄", callback_data= "chek_sub")
        ]
    ]
)