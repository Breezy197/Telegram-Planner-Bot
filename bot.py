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
    This handler will be called when user sends `/start` command
    """
    await message.reply("Привет! Я - бот планировщик задач, могу тебе напоминать о выполнении какой-то задачи",
                        reply_markup=kb.add_kb)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply("Тут будет инструкция")


@dp.message_handler()
async def help_command(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply("Тут будет инструкция")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
