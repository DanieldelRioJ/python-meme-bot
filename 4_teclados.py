from telegram import Update, ChatAction, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler
from telegram.files.inputmedia import InputMediaPhoto
from telegram.error import BadRequest

from random import randrange

memes = open("memes.txt").read().splitlines()

#callback /meme
def request_meme(update: Update, callback_context: CallbackContext) -> None:
    
    #Notificamos envío de foto
    update.message.reply_chat_action(ChatAction.UPLOAD_PHOTO)
    
    #Creamos el teclado para adjuntar
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Siguiente meme", callback_data="other")]])
    
    #Enviamos foto
    meme = memes[randrange(len(memes))]
    update.message.reply_photo(meme, caption = "Toma un meme", reply_markup=keyboard)
    
    
#callback clicar boton
def request_other_meme(update: Update, callback_context: CallbackContext) -> None:
    
    #Notificamos envío de foto
    update.callback_query.message.reply_chat_action(ChatAction.UPLOAD_PHOTO)
    
    #Creamos el teclado para adjuntar
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Siguiente meme", callback_data="other")]])
    
    #Enviamos foto
    meme = memes[randrange(len(memes))]
    try: 
        #Si la foto que nos saca el aleatorio es la misma, salta el error BadRequest (mensaje no modificado)
        update.callback_query.message.edit_media(InputMediaPhoto(meme), reply_markup=keyboard)
    except BadRequest:
        pass
    update.callback_query.answer()


def main() -> None:

    # Instancia un Updater y pasale el token del BOT
    updater = Updater("TOKEN")

    # Obten el dispatcher para anhadir handlers
    dispatcher = updater.dispatcher
   
    # TODO: ADD HANDLERS
    dispatcher.add_handler(CommandHandler("meme", request_meme))
    dispatcher.add_handler(CallbackQueryHandler(request_other_meme, pattern = "other"))
    
    # Arranca el bot
    updater.start_polling()

    #Bloquea la ejecución hasta pulsar Ctrl + C
    updater.idle()


if __name__ == '__main__':
    main()