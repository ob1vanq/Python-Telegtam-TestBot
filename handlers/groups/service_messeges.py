from loader import dp, bot
from aiogram import types




@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_members(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f"Пользователь {members} присоеденился к чату.")

@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def left_members(message: types.Message):
    if message.from_user.id == message.left_chat_member.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} покинул чат.")
    elif message.from_user.id == (await bot.me).id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} был удален ботом.")
    else:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} был удален пользователем "
                             f"{message.from_user.get_mention(as_html=True)}.")