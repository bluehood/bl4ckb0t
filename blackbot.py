from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
import callbacks as cb

# setup logging
fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=fmt, level=logging.INFO)


# setup bot
updater = Updater(token='inset token')
dispatcher = updater.dispatcher

dispatcher.add_error_handler(cb.error_callback)

start_handler = CommandHandler('start', cb.start)
dispatcher.add_handler(start_handler)

gerry_handler = CommandHandler('nodai', cb.no_dai_Geeeeerry)
dispatcher.add_handler(gerry_handler)

talk_handler = MessageHandler([Filters.text], cb.talk)
dispatcher.add_handler(talk_handler)


# start bot
updater.start_polling()
