import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import AdminFilter, IsGroup
from loader import dp


@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(message: types.Message):
    try:
        message_link = message.reply_to_message
        photo = message_link.photo[-1]
        photo = await photo.download(destination=io.BytesIO())
        input_file = types.InputFile(path_or_bytesio=photo)
        await message.chat.set_photo(photo=input_file)
    except:
        pass


@dp.message_handler(IsGroup(), Command("set_title", prefixes="!/"), AdminFilter())
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    await message.chat.set_title(title=source_message.text)


@dp.message_handler(IsGroup(), Command("set_description", prefixes="!/"), AdminFilter())
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    await message.chat.set_description(description=source_message.text)
