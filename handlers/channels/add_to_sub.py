
from loader import dp, bot
from aiogram import types

from data.config import channels
from filters import IsForwarded, IsPrivate
from keyboards.inline.add_chanel import add_to_chanel
from utils.misc import subs

current_channel_data = []

@dp.message_handler(IsForwarded(), IsPrivate(), content_types=types.ContentType.ANY)
async def get_channel_info(message: types.Message):
    await message.answer(f"Сообщение прислано из: {message.forward_from_chat.title}\n"
                         f"Username: {message.forward_from_chat.username}\n"
                         f"Id: {message.forward_from_chat.id}\n\n"
                         f"⚠ Убедитесь что Бот состоит в канале, прежде чем добавить его в список",
                         reply_markup=add_to_chanel)
    current_channel_data.append(message.forward_from_chat)

@dp.callback_query_handler(text="add_to_chanels")
async def add_to_channels(call: types.CallbackQuery):
    channel = current_channel_data[-1]
    if channel.id not in channels:
        channels.append(channel.id)
        chanel_list = str()
        for chan in channels:
            chanel_list += f"{chan}\n"
        await call.message.edit_text(f"Канал {channel.title} добавлен в список ✅\n\n"
                                  f"{chanel_list}", reply_markup=None)
    else:
        await call.answer(f"Канал {channel.title} уже добавлен в список.", show_alert=True)
        await call.message.edit_reply_markup()


@dp.callback_query_handler(text="do_not_chanels")
async def add_to_channels(call: types.CallbackQuery):
    await call.message.edit_reply_markup()



