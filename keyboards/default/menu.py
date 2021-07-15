from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Что-либо"),
            KeyboardButton(text="Нечто другое")
        ],
        [
            KeyboardButton(text="Отмена")

        ]
    ],
    resize_keyboard=True
)
