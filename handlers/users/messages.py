from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from keyboards.inline.main_btns import UserButton
from keyboards.one_time_keyboards import keyboards, button
from loader import dp, bot
from shortcuts.main_shortcuts import send_message_to_admin, filter_data
from shortcuts.weather_info import get_weather_by_location
from states.StatesGroup import Weather, Chat
from utils.db_api.manage import sentMessages


@dp.message_handler(Text(contains='Написать'))
async def answer(msg: Message, state: FSMContext):
    message = await msg.answer('Напиши что нибудь!\n'
                               'Анонимное сообщение: /anonymous\n'
                               'Отменить: /cancel')
    await state.update_data(message_id=message.message_id)
    await state.set_state(Chat.get_private_msg_to_admin.state)


@dp.message_handler(state=Chat.get_private_msg_to_admin.state)
async def answer(msg: Message, state: FSMContext):
    message_id = (await state.get_data()).get('message_id')
    await bot.delete_message(chat_id=msg.from_user.id, message_id=message_id)

    if 'cancel' in msg.text:
        await state.finish()
        return
    if 'anonymous' in msg.text:
        message = await msg.answer('Напишите сообщение.\n'
                                   '!Ваше имя не будет указано\n'
                                   'Отмена: /cancel')
        await state.update_data(message_id=message.message_id)
        await state.set_state(Chat.get_anonymous_msg_to_admin.state)
        return

    result = await send_message_to_admin(msg, name=msg.from_user.full_name)
    if result:
        await msg.answer('Отправлено!', reply_markup=button('Посмотреть', f'{msg.message_id}', 'see-sent_msg'))
    else:
        await msg.answer('Сообщение не отправлено!\n'
                         'Возникла ошибка при попытке отправить сообщение.')
    await state.finish()


@dp.message_handler(state=Chat.get_anonymous_msg_to_admin.state)
async def answer(msg: Message, state: FSMContext):
    message_id = (await state.get_data()).get('message_id')
    if 'cancel' in msg.text:
        await bot.delete_message(chat_id=msg.from_user.id, message_id=message_id)
        await state.finish()
        return
    result = await send_message_to_admin(msg)
    if result:
        await bot.edit_message_text(chat_id=msg.from_user.id, message_id=message_id, text='Отправлено!',
                                    reply_markup=button('Посмотреть', f'{msg.message_id}', 'see-sent_msg'))
        await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id)
    await state.finish()


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('see-sent_msg'))
async def seeSentMessage(call: CallbackQuery):
    message_id = filter_data(call.data, 'see-sent_msg')

    data = sentMessages(message_id).get()
    await call.answer(f'От пользователя: {data[1]}\n'
                      f'Кому: {data[2]}\n'
                      f'Сообщение: {data[3]}\n'
                      f'Время: {data[4]}', show_alert=True)


