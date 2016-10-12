# -*- coding: utf-8 -*-
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          CallbackQueryHandler)
import handlers as hnd
from quote_handler import QuoteHandler


def main():
    # create bl4ckst0ne
    updater = Updater('insert token')
    dp = updater.dispatcher

    # register handlers
    dp.add_handler(CommandHandler('start', hnd.start))
    dp.add_handler(CommandHandler('nodai', hnd.no_dai_Geeeeerry))
    dp.add_handler(CommandHandler('speak', hnd.speak, pass_args=True))
    dp.add_handler(MessageHandler([Filters.text], hnd.talk))
    dp.add_error_handler(hnd.print_error_info)
    #dp.add_handler(MessageHandler([], hnd.print_msg_info))

    q = QuoteHandler()
    dp.add_handler(CommandHandler('addaquote', q.prompt_user), group=1)
    dp.add_handler(MessageHandler([Filters.text], q.handle_new_quote), group=1)
    dp.add_handler(CallbackQueryHandler(q.save_quote), group=1)
    dp.add_handler(CommandHandler('tellaquote', q.tell_a_quote), group=1)

    # start LCMbot
    updater.start_polling()

    # run until the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
