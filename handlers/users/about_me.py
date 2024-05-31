from keyboards.inline.about_keyboards import aboutKb
from loader import dp, bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text(contains='about'))
async def aboutHandler(msg: Message):
    await msg.answer('''
    Меня зовут Йигиталиев Шохрух, мне 19 лет, в настоящее время я обучаюсь на программе высшего образования по направлению "Искусственный интеллект" в техническом университете города Ташкент.\nМои интересы включают информационные технологии, в основном я заинтересован в областях веб-программирования, машинного обучения, программирования микроконтроллеров Arduino и многих других.\nТакже я интересуюсь точными науками, такими как физика, астрономия и космология.\nВ свободное время я люблю фотографировать природу и делиться лучшими снимками в различных социальных сетях.
    ''', reply_markup=aboutKb())
