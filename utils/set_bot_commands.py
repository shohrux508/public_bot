from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Перезапустить бота"),
            types.BotCommand('about', "Подробнее обо мне"),
            types.BotCommand('assess', 'Обратная связь(анонимная оценка)'),
        ]
    )
