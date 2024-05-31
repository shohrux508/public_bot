from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class AdminKeyboard():
    def main(self):
        kb1 = KeyboardButton(text='Отправить сообщение')
        kb2 = KeyboardButton(text='Пользователи')
        kb4 = KeyboardButton(text='Мой кабинет')
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(kb1, kb2).add(kb4)
        return keyboard

