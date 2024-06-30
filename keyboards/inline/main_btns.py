from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import bot
from utils.db_api.check import is_required

btn = InlineKeyboardButton(text='❌', callback_data='remove-btn')


class AdminButton():

    def manage_sent_messages(self, message_id, count):
        btn1 = InlineKeyboardButton(text='Изменить сообщение', callback_data=f'edit-sent-msgs{message_id}+{count}')
        btn2 = InlineKeyboardButton(text='Удалить сообщение', callback_data=f'delete-sent-msgs{message_id}+{count}')
        keyboard = InlineKeyboardMarkup().add(btn1).add(btn2)
        return keyboard

    def manage_users_list(self, sort_by, filter_by, page, paginate_by):
        str = f'{sort_by}+{filter_by}+{page}+{paginate_by}'
        btn1 = InlineKeyboardButton(text='⬅️', callback_data=f'prev-page{str}')
        btn2 = InlineKeyboardButton(text='➡️', callback_data=f'next-page{str}')
        btn3 = InlineKeyboardButton(text='Все пользователи', callback_data=f'filter-by-users')
        btn4 = InlineKeyboardButton(text='Администраторы👨‍🚀', callback_data=f'filter-by-admins')
        btn5 = InlineKeyboardButton(text='Чёрный список', callback_data=f'filter-by-blocked-users')
        btn6 = InlineKeyboardButton(text='Искать 🔍', callback_data=f'search-user')
        btn7 = InlineKeyboardButton(text='Обновить', callback_data=f'refresh')
        keyboard = InlineKeyboardMarkup().add(btn1, btn6, btn2).add(btn3).add(btn4).add(btn5)
        return keyboard

    async def manage_channel(self, channel_id):
        if is_required(channel_id):
            btn = InlineKeyboardButton(text='Удалить из списка обязательной подписки❌',
                                       callback_data=f'set_required0+{channel_id}')
        else:
            btn = InlineKeyboardButton(text='Добавить в список обязательной подписки✅',
                                       callback_data=f'set_required1+{channel_id}')
        link = await bot.export_chat_invite_link(chat_id=channel_id)
        btn3 = InlineKeyboardButton(text='Открыть ', url=link)
        btn4 = InlineKeyboardButton(text='Удалить', callback_data=f'delete-channel{channel_id}')
        keyboard = InlineKeyboardMarkup().add(btn3, btn4).add(btn)
        return keyboard


class UserButton():
    def __init__(self, user_id):
        self.user_id = user_id




def detail_btns(id):
    btn1 = InlineKeyboardButton(text='Посмотреть', callback_data=f'detail{id}')
    btn2 = InlineKeyboardButton(text='Удалить', callback_data=f'delete{id}')
    keyboard = InlineKeyboardMarkup().add(btn1).add(btn2)
    return keyboard

