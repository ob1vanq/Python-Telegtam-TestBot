from aiogram import types
from aiogram.dispatcher.filters import Command


from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(Command("help"))
async def bot_help(message: types.Message):
    await message.answer("Bot commands:\n\n"
                         "/start - start bot\n"
                         "/help - view the list of command\n\n"
                         "Temporary commands:\n\n"
                         "/items - udemy test"
                         )
