from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("create_post", "action")

confirm_post = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Отправить", callback_data=post_callback.new(action = "post")),
            InlineKeyboardButton(text="Отклонить", callback_data=post_callback.new(action = "cancel"))
        ]
    ]
)


