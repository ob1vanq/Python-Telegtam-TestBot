from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default.location_keyboard import location
from loader import dp
from utils.misc.calc_distance import shortest_location


@dp.message_handler(Command("show_on_map"))
async def show_on_map(message: types.Message):
    await message.answer(
        text=f"Для определения местоположения воспользуйтесь кнопкой",
        reply_markup=location
    )

@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_location(message: types.Message):
    location = message.location
    lat = location.latitude
    lon = location.longitude
    closest_shops = shortest_location(location)

    text_format = "Название: <a href = '{url}'>{shop_name}</a>.\n" \
                  "Расстоянние до него: {distance:.1f} км."

    text = "\n\n".join(
        [
            text_format.format(shop_name = shop_name, url = url, distance = distance)
            for shop_name, distance,url, shop_location in closest_shops
        ]
    )

    await message.answer(f"Данные о месте 🗺:\n\n"
                         f"Latitude: <pre>{lat}</pre>\n"
                         f"Longitude: <pre>{lon}</pre>\n\n"
                         f"{text}",
                         disable_web_page_preview=True,
                         reply_markup=types.ReplyKeyboardRemove())

    for shop_name, distance,url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])
 