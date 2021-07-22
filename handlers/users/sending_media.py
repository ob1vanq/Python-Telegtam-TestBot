from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, MediaGroup

from loader import dp


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def photo_message(message: types.Message):
    await message.reply(f"{message.video.file_id}")


@dp.message_handler(Command("send_cat"))
async def send_cat(message: types.Message):
    photo_file_id = "AgACAgQAAxkBAAIQJ2D5adl7m2Uvjmx6MiMjSuwKTx0gAAIarDEbdky9UlMd5R_q4eszAQADAgADdwADIAQ"
    await message.answer_photo(photo=photo_file_id, caption="Вот кот, попробуй /more_cats")

@dp.message_handler(Command("more_cats"))
async def send_more_cats(message: types.Message):
    album = MediaGroup()
    cat_1 = "AgACAgQAAxkBAAIQJ2D5adl7m2Uvjmx6MiMjSuwKTx0gAAIarDEbdky9UlMd5R_q4eszAQADAgADdwADIAQ"
    cat_2 = "https://diapazon.kz/files/post/images/2016-09/original/lFtiRqzBS28B.jpg"
    video_cat = "BAACAgIAAxkBAAIQMWD5bBaSEFwYhJy9ei9ZB3Ehhy6nAAI5DgACJG3QSk-Sn00AAaQNtiAE"

    album.attach_photo(cat_1)
    album.attach_photo(cat_2)
    album.attach_video(video_cat, caption="Вот такие коты")

    await message.answer_media_group(media=album)