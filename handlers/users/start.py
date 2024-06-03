import requests as r
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from data.database import host
from keyboards.default.main import StartKeyboard
from loader import dp, bot
from shortcuts.main_shortcuts import filter_data
from utils.db_api.manage import ManageUser

#test
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
        print(response)
        await bot.send_message(chat_id=5016643462, text=f'Новый кент: {msg.from_user.full_name}')
        await msg.answer(f'Привет! {msg.from_user.first_name}.\n', reply_markup=StartKeyboard(msg.from_user.id).keyboard())
        await msg.answer('/menu <- Загляни сюда!')
    else:
        await msg.answer(f'Привет!', reply_markup=StartKeyboard(msg.from_user.id).keyboard())


@dp.message_handler(Text(contains='menu'))
async def menuHander(msg: Message):
    await msg.answer('Хочешь узнать больше обо мне? Тогда нажимай -> /about\nЗнаешь меня? Попробуй это -> /assess')




@dp.callback_query_handler(lambda x: x.data and x.data.startswith('remove-btn'))
async def remove_btn(call: CallbackQuery):
    msg_id = filter_data(call.data, 'remove-btn')
    if msg_id and msg_id != 'None':
        await bot.delete_message(chat_id=call.from_user.id, message_id=msg_id)
    await call.answer('❌')
    await call.message.delete()
