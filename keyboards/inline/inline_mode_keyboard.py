from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

keyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Поделится 🔮",
                                 switch_inline_query="")
        ]
    ]
)

keyboard2 = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Нажать",
                                 switch_inline_query_current_chat="")
        ]
    ]
)
