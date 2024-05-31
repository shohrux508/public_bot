from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



class UserKeyboard():

    def main(self):
        kb1 = KeyboardButton(text='Написать сообщение✏️')
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(kb1)
        return keyboard

    def settings(self):
        kb1 = KeyboardButton(text='Изменить номер телефона')
        kb3 = KeyboardButton(text='Сменить язык')
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(kb1, kb3).add(kb2)
        return keyboard


def share_phone():
    kb = KeyboardButton(text='Поделиться', request_contact=True)
    return ReplyKeyboardMarkup().add(kb)

