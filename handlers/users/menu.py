from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from filters import IsPrivate
from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("menu"), IsPrivate())
async def show_menu(message: types.Message):
    await message.answer("Выбери что-либо", reply_markup=menu)


@dp.message_handler(Text(equals=["Что-либо", "Нечто другое"]))
async def choise_something(message: types.Message):
    await message.answer(f"Поздравляю! Вы что-то выбрали...{message.text}",reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Отмена")
async def close_keyboard(message: types.Message):
    await message.answer(text="Вы отменили выбор", reply_markup=ReplyKeyboardRemove())
