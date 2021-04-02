from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_add = KeyboardButton('Добавить напоминание')
button_plan = KeyboardButton('Посмотреть расписание')

add_kb = ReplyKeyboardMarkup().add(button_add).add(button_plan)
