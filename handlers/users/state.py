from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import state_question
from loader import dp
from states import udemy_test


@dp.message_handler(commands="form")
async def enter_test(message: types.Message):
    await message.answer("Выберите действие", reply_markup=state_question)




@dp.message_handler(text="Перезаписать данные")
async def enter_test(message: types.Message):
    await message.answer("1. Введите свое Имя: ", reply_markup=ReplyKeyboardRemove())
    await udemy_test.first()


@dp.message_handler(state=udemy_test.name_state)
async def answer_name(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer_name"] = answer
    await message.answer("2. Введите свой email: ")
    await udemy_test.next()


@dp.message_handler(state=udemy_test.email_state)
async def answer_email(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer_email"] = answer
    await message.answer("3. Введите номер мобильного телефона: ")
    await udemy_test.next()


@dp.message_handler(state=udemy_test.phone_number_state)
async def answer_email(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer_ph_number"] = answer
    data = await state.get_data()
    answer_name = data.get("answer_name")
    answer_email = data.get("answer_email")
    answer_ph_number = data.get("answer_ph_number")

    await message.answer("Ты ввел следующие данные:\n\n"
                         f"Имя - \"`{answer_name}`\"\n\n"
                         f"Email - \"`{answer_email}`\"\n\n"
                         f"Телефон: - \"`{answer_ph_number}`\"", parse_mode="Markdown", reply_markup=state_question
                         )
    await state.reset_state(with_data=False)

@dp.message_handler(text="Посмотреть данные")
async def enter_test(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer_name = data.get("answer_name")
    answer_email = data.get("answer_email")
    answer_ph_number = data.get("answer_ph_number")
    await message.answer(f"Имя - \"`{answer_name}`\"\n"
                         f"Email - \"`{answer_email}`\"\n"
                         f"Телефон: - \"`{answer_ph_number}`\"", parse_mode="Markdown"
                         )

@dp.message_handler(text="Выход")
async def close_keyboard(message: types.Message,state: FSMContext):
    await message.answer(text="Выход совершен успешно", reply_markup=ReplyKeyboardRemove())
