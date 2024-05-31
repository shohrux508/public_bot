from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup





def aboutKb():
    kb1 = InlineKeyboardButton(text='Instagram', url='https://instagram.com/shohrux.yigitaliev')
    kb2 = InlineKeyboardButton(text='Telegram канал(личный блог)', url='https://t.me/shohrux_yigitaliev')
    kb3 = InlineKeyboardButton(text='Git Hub', url='https://github.com/shohrux508')
    keyboard = InlineKeyboardMarkup().add(kb1).add(kb2).add(kb3)
    return keyboard
