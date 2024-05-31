import time

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from keyboards.one_time_keyboards import keyboards, button
from shortcuts.main_shortcuts import filter_data
from states.StatesGroup import assessmentStates
from utils.db_api.manage import ManageUser


@dp.message_handler(Text(contains='assess'))
async def estimateHandler(msg: Message, state: FSMContext):
    await msg.answer(
        'Если мы с вами знакомы или вы меня знаете, то буду рад видеть вашу оценку! Ваше мнение поможет мне стать еще лучше.',
        reply_markup=button('Оценить ', '', 'assess'))


@dp.callback_query_handler(lambda x: x.data and 'assess' in x.data)
async def assessHandler(call: CallbackQuery, state: FSMContext):
    time.sleep(2)
    await call.answer(
        'Ваши сообщения будут полностью анонимными, если хотите связаться напрямую, вы можете сделать это написав сообщение.\nТакже вы можете предлагать свои идеи для улучшения бота/',
        show_alert=True)
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text='''1. Что в моем общении с вами вам больше всего нравится?\n
2. Как я могу улучшить наше общение?\n
3. Какие мои качества вы цените больше всего?\n
4. Есть что-то, что я делаю, что может раздражать вас?\n
5. Какие аспекты моей личности или поведения вас интересуют/вдохновляют?\n\n /cancel -> Отменить''')
    await state.update_data(message_id=call.message.message_id)
    await state.set_state(assessmentStates.first.state)


@dp.message_handler(state=assessmentStates.first.state)
async def assessHandlerFirst(msg: Message, state: FSMContext):
    message_id = (await state.get_data()).get('message_id')
    if 'cancel' in msg.text:
        await bot.edit_message_text(chat_id=msg.from_user.id, message_id=message_id, text='Отменено!')
        await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id)
        await state.finish()
        return
    list = ManageUser(msg.from_user.id).list(select_id=True, filter_by='admin')
    for id in list:
        text = (f'Анонимная оценка:\n{msg.text}')
        await bot.send_message(chat_id=id, text=text)
    await state.finish()
    await msg.answer('Ваше сообщение было отправлено(анонимно), спасибо!')
