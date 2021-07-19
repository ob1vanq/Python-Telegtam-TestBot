from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Начать работу с ботом"),
            types.BotCommand("menu", "Тест ReplyKeyboardMarkup"),
            types.BotCommand("buy", "Тест InlineKeyboardMarkup"),
            types.BotCommand("is_true", "Доступно в инлайн режиме"),
            types.BotCommand("get_update", "Посмотреть данные чата"),
        ]
    )

