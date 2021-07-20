from aiogram import types

from loader import  dp, bot

@dp.channel_post_handler(content_types=types.ContentType.ANY)
async def new_post(message: types.Message):
   from data.config import admins
   admin = admins[0]
   try:
       await bot.send_message(chat_id=admin,
                              text= f"В канале {message.chat.title} опубликован "
                                    f"<a href = '{await message.chat.get_url()}'> пост</a>:\n\n"
                                    f"{message.text}")
   except:
       pass




