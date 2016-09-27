# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import handlers as hnd


# enable logging
fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=fmt, level=logging.INFO)


def main():
    # create bl4ckst0ne
    updater = Updater('insert token')
    dp = updater.dispatcher

    # register handlers
    dp.add_handler(CommandHandler('start', hnd.start))
    dp.add_handler(CommandHandler('nodai', hnd.no_dai_Geeeeerry))
    dp.add_handler(CommandHandler('speak', hnd.speak))
    dp.add_handler(MessageHandler([Filters.text], hnd.talk))
    dp.add_error_handler(hnd.print_error_info)
    #dp.add_handler(MessageHandler([], hnd.print_msg_info))

    # start LCMbot
    updater.start_polling()

    # run until the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
