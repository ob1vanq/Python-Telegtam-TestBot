from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.callback_datas import buy_item
from keyboards.inline.toBuy import BuyMarkup, ChoseItem
from loader import dp


@dp.message_handler(Command("buy"))
async def buy_start_message(message: types.Message):
    await message.answer(text="Это меню покупки товара", reply_markup=BuyMarkup)


@dp.callback_query_handler(text="cancel")
async def buy_cancel(call: types.CallbackQuery):
    await call.answer(text="Вы отменили покупку", show_alert=True)
    await call.message.edit_text(text="Покупка отменена пользователем.", reply_markup=None)


@dp.callback_query_handler(text="buy")
async def buy_chose_item(call: types.CallbackQuery):
    await call.message.edit_text(text="Выберите один из доступных товаров: \n"
                                      "\t🍎 Яблоко \n"
                                      "\t🍐 Груша",reply_markup=ChoseItem)


@dp.callback_query_handler(buy_item.filter(item="pear"))
async def buy_cancel(call: types.CallbackQuery):
    await call.message.edit_text("Вы купили Грушу", reply_markup=None)


@dp.callback_query_handler(buy_item.filter(item="apple"))
async def buy_cancel(call: types.CallbackQuery):
    await call.message.edit_text("Вы купили Яблоко", reply_markup=None)
