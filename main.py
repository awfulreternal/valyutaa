from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Замените на свой токен, полученный у @BotFather
TOKEN = 'your_bot_token_here'

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я игровой бот GRAM. Начнем игру!')

# Обработчик команды /help
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Это игровой бот GRAM. Он поможет вам провести время с удовольствием!')

def main() -> None:
    # Инициализируем Updater с токеном бота
    updater = Updater(TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
