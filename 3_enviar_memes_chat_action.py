from telegram import Update, ChatAction, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, error, InlineQueryResultPhoto
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler, InlineQueryHandler

from random import randrange

memes = open("memes.txt").read().splitlines()

#callback /meme
def request_meme(update: Update, callback_context: CallbackContext) -> None:
    
    #Notificamos envío de foto
    update.message.reply_chat_action(ChatAction.UPLOAD_PHOTO)
    
    #Enviamos foto
    meme = memes[randrange(len(memes))]
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Siguiente meme", callback_data="other")]])
    update.message.reply_photo(meme, reply_markup=keyboard)
    
    
def request_other_meme(update: Update, callback_context: CallbackContext) -> None:
    
    #Enviamos foto
    meme = memes[randrange(len(memes))]
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Siguiente meme", callback_data="other")]])
    try:
        update.callback_query.message.edit_media(InputMediaPhoto(meme), reply_markup=keyboard)
    except error.BadRequest:
        pass
    update.callback_query.answer()


def inline_callback(update: Update, callback_context: CallbackContext) -> None:
    
    results = [InlineQueryResultPhoto(str(i), meme, thumb_url=meme, caption ="Un meme gracioso") for i, meme in enumerate(memes)]
    update.inline_query.answer(results)

def main() -> None:
    
    # Instancia un Updater y pasale el token del BOT
    updater = Updater("TOKEN")

    # Obten el dispatcher para anhadir handlers
    dispatcher = updater.dispatcher

    # TODO: ADD HANDLERS
    
    dispatcher.add_handler(CallbackQueryHandler(request_other_meme, pattern="other"))
    dispatcher.add_handler(CommandHandler("meme", request_meme))
    dispatcher.add_handler(InlineQueryHandler(inline_callback))
    
    # Arranca el bot
    updater.start_polling()

    #Bloquea la ejecución hasta pulsar Ctrl + C
    updater.idle()


if __name__ == '__main__':
    main()