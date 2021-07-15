from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

state_question = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton("Перезаписать данные")
        ],
        [
          KeyboardButton("Посмотреть данные")
        ],
        [
            KeyboardButton("Выход")
        ]
    ],
    resize_keyboard=True
)