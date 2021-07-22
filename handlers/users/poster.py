from aiogram import types
from aiogram.dispatcher.filters import Command

from data import admins
from data.config import channels
from filters import AdminFilter
from keyboards.inline.confirm_keyboard import confirm_post, post_callback
from loader import dp, bot
from states import SugPost
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(Command("suggest_post"))
async def suggest_post(message: types.Message):
    await message.answer("Отправьте пост для публикации.")
    await SugPost.EnterMessage.set()


@dp.message_handler(state=SugPost.EnterMessage)
async def enter_post(message: types.Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention(as_html=True))
    await message.answer("Вы собираетесь отправить пост на проверку?",
                         reply_markup=confirm_post)
    await SugPost.next()


@dp.callback_query_handler(post_callback.filter(action="post"), state=SugPost.Confirm)
async def confrim_post(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        mention = data.get("mention")

    await state.finish()
    await call.message.edit_text("Вы отправили пост на проверку.")

    await bot.send_message(chat_id=admins[0], text=f"Пользователь {mention} "
                                                   f"отправил пост на проверку: ")
    await bot.send_message(chat_id=admins[0], text=text, parse_mode="HTML",
                           reply_markup=confirm_post)


@dp.callback_query_handler(post_callback.filter(action="cancel"))
async def cancel_post(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text("Вы отклонили пост.")


@dp.message_handler(state=SugPost.Confirm)
async def unknow_post(message: types.Message):
    await message.answer("Выберите отправить или отклонить пост")


@dp.callback_query_handler(post_callback.filter(action="post"), user_id=admins)
async def confirm_admin_post(call: types.CallbackQuery):
    await call.answer("Вы одобрили этот пост", show_alert=True)

    try:
        target_channel = channels[0]
        message = await call.message.edit_reply_markup()
        await message.send_copy(chat_id=target_channel)
    except:
        await call.message.answer("⚠️Список каналов пуст. Пост не отправлен")


@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=admins)
async def cancel_admin_post(call: types.CallbackQuery):
    await call.answer("Пост отменен", show_alert=True)
    await call.message.edit_reply_markup()
