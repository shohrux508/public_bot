import requests as r
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from data.database import host
from keyboards.default.main import StartKeyboard
from loader import dp, bot
from shortcuts.main_shortcuts import filter_data
from utils.db_api.manage import ManageUser


@dp.message_handler(CommandStart())
async def start(msg: Message):
    if ManageUser(msg.from_user.id).is_user() == False:
        ManageUser(msg.from_user.id).new(full_name=msg.from_user.full_name, phone='*', is_admin=0, is_blocked=0,
                                         language='ru')
        data = {
            "name": f"{msg.from_user.full_name}",
            "telegram_id": f"{msg.from_user.id}",
            "phone": f"*",
        }
        response = r.post(url=f'{host}/myserver/users/new/', data=data)
        await msg.answer('Привет! Это мой личный бот. Тут вы можете узнать подробнее обо мне /about или связаться со мной.\n', reply_markup=StartKeyboard(msg.from_user.id).keyboard())
    else:
        await msg.answer(f'Привет! {msg.from_user.first_name}', reply_markup=StartKeyboard(msg.from_user.id).keyboard())






@dp.callback_query_handler(lambda x: x.data and x.data.startswith('remove-btn'))
async def remove_btn(call: CallbackQuery):
    msg_id = filter_data(call.data, 'remove-btn')
    if msg_id and msg_id != 'None':
        await bot.delete_message(chat_id=call.from_user.id, message_id=msg_id)
    await call.answer('❌')
    await call.message.delete()
