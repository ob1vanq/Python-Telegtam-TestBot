from loader import dp, bot
from aiogram import types

from aiogram.dispatcher.filters import Command
from keyboards.inline.chek_sub import ChekSub
from utils.misc import subs
from data.config import channels
from filters import IsPrivate




@dp.message_handler(Command("channels"), IsPrivate())
async def show_channels(message: types.Message):
    chanels_format = str()
    for channel in channels:
        chat = await bot.get_chat(channel)
        invite_link = await  chat.export_invite_link()
        chanels_format += f"Канал <a href ='{invite_link}'> {chat.title} </a>\n"
    await message.answer(f"Подпишитесь на следующие каналы: \n\n"
                         f"{chanels_format}",
                         reply_markup=ChekSub, disable_web_page_preview=True)


@dp.callback_query_handler(text="chek_sub")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str("Подпишитесь на следующие каналы: \n\n")
    for channel in channels:
        status = await subs.chek(user_id=call.from_user.id,
                                 channel=channel)
        channel = await bot.get_chat(channel)
        invite_link = await channel.export_invite_link()

        if status:
            result += f"✅ Подписка на канал <a href ='{invite_link}'> {channel.title} </a> оформлена\n"

        else:
            result += f"❌ Подписка на канал <a href ='{invite_link}'> {channel.title} </a> не оформлена\n"


    await call.message.edit_text(result, disable_web_page_preview=True, reply_markup=ChekSub)
