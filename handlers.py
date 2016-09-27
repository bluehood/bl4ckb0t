# -*- coding: utf-8 -*-
import numpy as np
from random import random as rand
from time import sleep
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, NetworkError)
from behaviours import behaviours


def start(bot, update):
    """ Start off with an anectode """
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Oh raga, l'altro giorno la vale mi fa 'oh raga'")


def no_dai_Geeeeerry(bot, update):
    """ Rebut Gerry's argument vigorously """
    voice_file_id = 'AwADBAADCwADzPSlEYhD8dBXfH8LAg'
    bot.sendVoice(chat_id=update.message.chat_id, voice=voice_file_id)


def talk(bot, update):
    """ Engage in meaningful conversation """
    text = update.message.text
    chat_id = update.message.chat_id

    # ad-hoc replies to interesting messages
    for bhv in behaviours:
        for s in bhv['trigger']:
            if s in text:
                rep_type = bhv['reply_type']
                reply = np.random.choice(bhv['reply'])
                if rep_type == 'text':
                    bot.sendMessage(chat_id=chat_id, text=reply)
                elif rep_type == 'sticker':
                    bot.sendSticker(chat_id=chat_id, sticker=reply)

    # random replies to uninteresting messages
    # prob. that at least one of these is sent every 10 mess. received is 0.57
    if rand() < 2./60.:
        # note: until we switch to async processing this is a time during which
        # bl4ckst0ne is completely paralysed
        secondsBeforeNagging = 15
        sleep(secondsBeforeNagging)
        bot.sendMessage(chat_id=chat_id,
                        text='oh raga ma la grigliata è confermata?')

    if rand() < 2./60.:
        vignati_hat = 'BQADBAADRAADnWzWBo9KlpThN0OQAg'
        vignati_bw = 'BQADBAADcQADnWzWBjwXcOqPvseKAg'
        stickers = [ vignati_hat, vignati_bw ]
        bot.sendSticker(chat_id=chat_id, sticker=stickers[int(rand() < 0.5)])


def print_msg_info(bot, update):
    """ Take notes - print logs to console """
    print update.message


def print_error_info(bot, update, error):
    """ Take notes - print errors to console """
    logger.warn('Update "%s" caused error "%s"' % (update, error))
