from telegram import Update, ChatAction
from telegram.ext import Updater, CallbackContext, CommandHandler

from random import randrange

memes = open("memes.txt").read().splitlines()

#callback /meme
def request_meme(update: Update, callback_context: CallbackContext) -> None:
    
    #Notificamos envío de foto
    update.message.reply_chat_action(ChatAction.UPLOAD_PHOTO)
    
    #Enviamos foto
    meme = memes[randrange(len(memes))]
    update.message.reply_photo(meme, caption = "Toma un meme")


def main() -> None:
    
    # Instancia un Updater y pasale el token del BOT
    updater = Updater("TOKEN")

    # Obten el dispatcher para anhadir handlers
    dispatcher = updater.dispatcher

    # TODO: ADD HANDLERS
    
    
    dispatcher.add_handler(CommandHandler("meme", request_meme))
    
    # Arranca el bot
    updater.start_polling()

    #Bloquea la ejecución hasta pulsar Ctrl + C
    updater.idle()


if __name__ == '__main__':
    main()