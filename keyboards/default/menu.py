from tkinter import Tk

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Указать свой номер", request_contact= True),
            KeyboardButton(text="Указать свою локацию", request_location = True)
        ],
        [
            KeyboardButton(text="Что-либо"),
            KeyboardButton(text="Нечто другое")
        ],

        [
            KeyboardButton(text="Отмена")

        ],
        [
            KeyboardButton(text="Создать опрос", request_poll=KeyboardButtonPollType())
        ]

    ],
    resize_keyboard=True,
    selective=True
)
