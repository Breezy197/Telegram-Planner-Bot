import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import keyboards as kb
import config
from access import AccessMiddleware

# Берем данные пользователя и бота из config.py
API_TOKEN = config.TOKEN
ACCESS_ID = config.ID

logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчер
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(AccessMiddleware(ACCESS_ID))

# Машина состояний
class States(StatesGroup):
    data = State()


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


@dp.message_handler(state=States.data)
async def help_command(message: types.Message, state: FSMContext):
    """
    Вызываем хендлер для обработки статуса принятия названия и даты напоминания
    """
    await state.update_data(date=message.text.lower())
    await state.finish()
    await message.reply("Ваше напоминание принято")


@dp.message_handler(lambda message: message.text == "Добавить напоминание")
async def add_command(message: types.Message):
    """
    Вызываем хендлер для обработки сообщения по добавлению напоминания
    """
    await States.data.set()
    await message.reply("Введите название и дату")


@dp.message_handler(lambda message: message.text == "Посмотреть расписание")
async def plan_command(message: types.Message):
    """
    Вызываем хендлер для обработки сообщения по выводу расписания на сегодня
    """
    await message.reply("Выводим расписание")


@dp.message_handler()
async def other_command(message: types.Message):
    """
    Вызываем хендлер для обработки несуществующих команд
    """
    await message.reply("Не знаю что ответить :(")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
