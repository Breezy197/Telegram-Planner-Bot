import logging

from aiogram import Bot, Dispatcher, executor, types

import keyboards as kb

API_TOKEN = '1791488192:AAH_DNEzMxsErxo0eo35yXYOYGoM67R93ro'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    Вызываеем хендлер для обработки команды start и приветствуем бота
    """
    await message.reply("Привет! Я - бот планировщик задач, могу тебе напоминать о выполнении какой-то задачи",
                        reply_markup=kb.add_kb)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    """
    Вызываеем хендлер для обработки команды help и выводим список функционала бота
    """
    await message.reply("Тут будет инструкция")


@dp.message_handler(lambda message: message.text == "Добавить напоминание")
async def help_command(message: types.Message):
    """
    Вызываем хендлер для обработки сообщения по добавлению напоминания
    """
    await message.reply("Добавляем дату")


@dp.message_handler(lambda message: message.text == "Посмотреть расписание")
async def help_command(message: types.Message):
    """
    Вызываем хендлер для обработки сообщения по выводу расписания на сегодня
    """
    await message.reply("Выводим расписание")


@dp.message_handler()
async def help_command(message: types.Message):
    """
    Вызываем хендлер для обработки несуществующих команд
    """
    await message.reply("Не знаю что ответить :(")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
