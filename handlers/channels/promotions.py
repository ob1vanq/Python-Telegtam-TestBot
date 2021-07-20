from aiogram.types import Chat

from loader import dp
from aiogram import types

from data.config import chanels
from filters import IsForwarded, IsPrivate
from keyboards.inline.add_chanel import add_to_chanel


@dp.message_handler(IsForwarded(), IsPrivate(), content_types=types.ContentType.ANY)
async def get_chanel_info(message: types.Message):
    global chanel
    chanel= message.forward_from_chat
    await message.answer(f"Сообщение прислано из: {message.forward_from_chat.title}\n"
                         f"Username: {message.forward_from_chat.username}\n"
                         f"Id: {message.forward_from_chat.id}", reply_markup=add_to_chanel)

@dp.callback_query_handler(text="add_to_chanels")
async def add_to_chanels(call: types.CallbackQuery):
    if chanel.id not in chanels:
        chanels.append(chanel.id)
        chanel_list = str()
        for chan in chanels:
            chanel_list += f"{chan}\n"
        await call.message.answer(f"Канал {chanel.title} добавлен в список ✅\n\n"
                                     f"{chanel_list}", reply_markup=None)
    else:
        await call.answer(f"Канал {chanel.title} уже добавлен в список.", show_alert= True)
        await call.message.edit_reply_markup()



@dp.callback_query_handler(text="do_not_chanels")
async def add_to_chanels(call: types.CallbackQuery):
    await call.message.edit_reply_markup()