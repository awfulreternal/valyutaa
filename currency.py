from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton

from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

import requests



# Токен вашего бота, полученный у @BotFather

TOKEN = '7294993191:AAG1bDTcYRV7hMXBkPDp7okapOwcjTDntA8'



# API ключ для доступа к данным курсов валют (замените на свой)

API_KEY = '7294993191:AAG1bDTcYRV7hMXBkPDp7okapOwcjTDntA8'



# URL API для получения курсов валют

API_URL = f'https://api.currencystack.io/latest?access_key={API_KEY}'



# Обработчик команды /start

def start(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(

        "Привет! Я бот, который предоставляет информацию о курсах валют.\n" +

        "Используйте команду /rates для получения текущих курсов."

    )



# Обработчик команды /rates

def rates(update: Update, context: CallbackContext) -> None:

    try:

        response = requests.get(API_URL)

        data = response.json()



        if response.status_code == 200:

            rates = data['rates']

            message = "Текущие курсы валют:\n"

            for currency, rate in rates.items():

                message += f"{currency}: {rate:.2f}\n"



            update.message.reply_text(message)

        else:

            update.message.reply_text("Не удалось получить курсы валют. Попробуйте позже.")

    except Exception as e:

        print(str(e))

        update.message.reply_text("Произошла ошибка при получении курсов валют. Попробуйте позже.")



# Обработчик неизвестных команд

def unknown(update: Update, context: CallbackContext) -> None:

    update.message.reply_text("Извините, такая команда не поддерживается.")



def main() -> None:

    updater = Updater(TOKEN, use_context=True)



    dispatcher = updater.dispatcher



    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(CommandHandler("rates", rates))

    dispatcher.add_handler(MessageHandler(Filters.command, unknown))



    updater.start_polling()



    updater.idle()



if __name__ == '__main__':

    main()



