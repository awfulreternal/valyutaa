import logging
from aiogram import Bot, Dispatcher, executor, types

# Замените на свой токен, полученный у @BotFather
TOKEN = '7294993191:AAEFCphfC1PraUbSkD8IyWvTEg6qGGyvAtQ'

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я игровой бот GRAM. Начнем игру!")

# Обработчик команды /help
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Это игровой бот GRAM. Он поможет вам провести время с удовольствием!")

def main():
    # Запускаем бота
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    main()
