from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from states.StatesGroup import postStates


@dp.message_handler(Text(contains='post'))
async def postHandler(msg: Message, state: FSMContext):
    message = await msg.answer('Жду ваше сообщение... - для публикации!\n'
                     'Отменить: /cancel')
    await state.update_data(message_id=message.message_id)
    await state.set_state(postStates.get_message.state)


@dp.message_handler(state=postStates.get_message.state, content_types=['text', 'photo', 'animation', 'video', 'audio'])
async def publicPost(msg: Message, state: FSMContext):
    message_id = (await state.get_data()).get('message_id')
    await state.finish()
    if msg.text:
        if 'cancel' in msg.text:
            await bot.delete_message(chat_id=msg.from_user.id, message_id=message_id)
            return
        await bot.send_message(chat_id=1865457293, text=msg.text)
    elif msg.photo:
        await bot.send_photo(chat_id=1865457293, photo=msg.photo, caption='photo-1')
    elif msg.video:
        await bot.send_video(chat_id=1865457293, video=msg.video, caption='video-1')
    elif msg.animation:
        await bot.send_animation(chat_id=1865457293, animation=msg.animation, caption='animation-1')
    await bot.forward_message(chat_id=1865457293, from_chat_id=msg.from_user.id, message_id=msg.message_id, protect_content=True, disable_notification=True)
    await msg.answer('Переслал!')

