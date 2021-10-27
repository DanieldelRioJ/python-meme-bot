from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler
from telegram.ext.filters import Filters

def callback_func(update: Update, callback_context: CallbackContext):
    text = update.message.text
    update.message.reply_text(text.upper())

def main() -> None:

    # Instancia un Updater y pasale el token del BOT
    updater = Updater("TOKEN")

    # Obten el dispatcher para anhadir handlers
    dispatcher = updater.dispatcher

    # TODO: ADD HANDLERS
    dispatcher.add_handler(MessageHandler(filters = Filters.all, callback = callback_func))
    
    # Arranca el bot
    updater.start_polling()

    #Bloquea la ejecución hasta pulsar Ctrl + C
    updater.idle()


if __name__ == '__main__':
    main()