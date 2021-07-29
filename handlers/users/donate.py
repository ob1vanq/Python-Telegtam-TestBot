from aiogram import types
from aiogram.dispatcher.filters import Command

from data.donate_item import Cookie, DONATE
from loader import dp, bot


@dp.message_handler(Command("donate"))
async def donate(message: types.Message):
    await bot.send_invoice(message.chat.id,
                           **Cookie.generete_invoice(),
                           payload="01",
                           suggested_tip_amounts=[ 15_00,40_00,90_00 ],
                           max_tip_amount=100_00)


@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    await bot.answer_shipping_query(shipping_query_id=query.id,shipping_options=[DONATE],
                                    ok=True)


@dp.pre_checkout_query_handler()
async def checkout_query(query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id,
                                        ok=True)
    await bot.send_message(chat_id=query.from_user.id, text=f"{query.from_user.full_name} Спасибо за донат ❤")
    await bot.send_message(chat_id=454793780, text=f"{query.from_user.get_mention(as_html=True)} прислал донат: "
                                                   f"<b>{str(query.total_amount)[:(len(str(query.total_amount))-2)]}.00</b>")
