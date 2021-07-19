import datetime
import re

from aiogram import types

from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import AdminFilter, IsGroup
from loader import dp


@dp.message_handler(IsGroup(), Command("ro", prefixes="!/"), AdminFilter())
async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    comand_parse = re.compile(r"(/ro|!ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = comand_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5
    else:
        time = int(time)


    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    ReadOnlyPermissions = types.ChatPermissions(
        can_send_polls=False,
        can_change_info=False,
        can_send_media_messages=False,
        can_invite_users=True,
        can_send_other_messages=False,
        can_pin_messages=False,
        can_send_messages=False,
        can_add_web_page_previews=False
    )
    try:
        await message.chat.restrict(user_id=member.id, permissions=ReadOnlyPermissions,
                                       until_date=until_date)
        await message.reply(f"Пользователю {member.get_mention(as_html=True)} заперщено писать на {time}"
                             f" минут, по причине: {comment}")
    except BadRequest:
        await message.answer(f"Пользователь {member.get_mention(as_html=True)} является администратором")

@dp.message_handler(IsGroup(), Command("unro", prefixes="!/"), AdminFilter())
async def undo_read_only_mode(message: types.Message):
    try:
        member = message.reply_to_message.from_user

        AllowedPermissions = types.ChatPermissions(
            can_send_polls=True,
            can_change_info=False,
            can_send_media_messages=True,
            can_invite_users=True,
            can_send_other_messages=True,
            can_pin_messages=False,
            can_send_messages=True,
            can_add_web_page_previews=True
        )

        await message.chat.restrict(user_id=member.id, permissions= AllowedPermissions, until_date=0)
        await message.reply(f"Пользователь {member.get_mention(as_html=True)} снова может писать.")
    except:
        pass

@dp.message_handler(IsGroup(), Command("ban", prefixes="!/"), AdminFilter())
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    try:
        await message.chat.kick(user_id=member.id)
        await message.reply(f"Пользователь {member.get_mention(as_html=True)} был забанен")
    except BadRequest:
        await message.answer(f"Пользователь {member.get_mention(as_html=True)} является администратором")

@dp.message_handler(IsGroup(), Command("unban", prefixes="!/"), AdminFilter())
async def unban_user(message: types.Message):
    try:
        member = message.reply_to_message.from_user
        await message.chat.unban(user_id=member.id)
        await message.reply(f"Пользователь {member.get_mention(as_html=True)} был разбанен")
    except:
        pass