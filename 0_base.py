from telegram import Update
from telegram.ext import Updater, CallbackContext

memes = open("memes.txt").read().splitlines()

def main() -> None:
    
    # Instancia un Updater y pasale el token del BOT
    updater = Updater("TOKEN")

    # Obten el dispatcher para anhadir handlers
    dispatcher = updater.dispatcher

    # TODO: ADD HANDLERS

    # Arranca el bot
    updater.start_polling()

    #Bloquea la ejecución hasta pulsar Ctrl + C
    updater.idle()


if __name__ == '__main__':
    main()