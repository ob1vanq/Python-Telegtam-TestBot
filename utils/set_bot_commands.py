from aiogram import types
from loguru import logger

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("menu", "Тест ReplyKeyboardMarkup"),
            types.BotCommand("buy", "Тест InlineKeyboardMarkup"),
            types.BotCommand("is_true", "⚠️Доступно в инлайн режиме"),
            types.BotCommand("get_update", "Посмотреть данные чата"),
            types.BotCommand("set_photo", "Установить новое фото группы"),
            types.BotCommand("set_title", "Установить новое название группы"),
            types.BotCommand("set_description", "Установить новое описание группы"),
            types.BotCommand("ro", "Запретить пользователю писать сообщения"),
            types.BotCommand("unro", "Разрешить пользователю писать сообщения"),
            types.BotCommand("ban", "Забанить пользователя (удаление)"),
            types.BotCommand("unban", "Разбанить пользователя")
        ]
    )
    logger.info("Установка комманд прошла успешно")
