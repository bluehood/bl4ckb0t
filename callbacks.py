# -*- coding: utf-8 -*-

import numpy as np
from random import random as rand
from time import sleep
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, NetworkError)


# /start
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Oh raga, l'altro giorno la vale mi fa 'oh raga'")


# /noDaiGeeeeeerry
def no_dai_Geeeeerry(bot, update):
    voice_file = 'AwADBAADCwADzPSlEYhD8dBXfH8LAg'
    bot.send_voice(chat_id=update.message.chat_id, voice=voice_file)


# replies to text messages
def talk(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id
    print update.message.from_user

    testicle_triggers = {
        'msg' : [ 'ho sbagliato', 'Ho sbagliato', 'Ah no', 'ah no' ],
        'reply_type' : 'text',
        'reply': [ 'Sei un cogliooooone' ]
    }
    gerry_triggers = {
        'msg' : [ 'no dai', 'No dai', 'dai no', 'Dai no' ],
        'reply_type' : 'text',
        'reply' : [ 'no dai geeeeerry' ]
    }
    stefy_triggers = {
        'msg' : [ 'no beh', 'No beh', 'forte', 'Forte', 'stefano', 'Stefano',
                  'stefy', 'Stefy', 'hamiltoniana', 'Hamiltoniana',
                  'autovalori' ],
        'reply_type' : 'sticker',
        'reply' : [ 'BQADBAADhQADnWzWBjYVjZV8OT1cAg',
                    'BQADBAADnwADnWzWBuBUlm_lDucyAg',
                    'BQADBAADnQADnWzWBj6GAtyTZtebAg' ]
    }

    # ad-hoc replies to interesting messages
    for trigger in [ testicle_triggers, gerry_triggers, stefy_triggers ]:
        for s in trigger['msg']:
            if s in text:
                reply = np.random.choice(trigger['reply'])
                rep_type = trigger['reply_type']
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
    elif rand() < 1./60.:
        bot.sendMessage(chat_id=update.message.chat_id,
                        text='Oh raga, l\'altro giorno la vale mi fa "oh raga"')

    if rand() < 2./60.:
        vignati_hat = 'BQADBAADRAADnWzWBo9KlpThN0OQAg'
        vignati_bw = 'BQADBAADcQADnWzWBjwXcOqPvseKAg'
        stickers = [ vignati_hat, vignati_bw ]
        bot.sendSticker(chat_id=chat_id, sticker=stickers[int(rand() < 0.5)])


# print all message info to console
def print_msg_info(bot, update):
    print update.message


# Error callbacks
def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized as e:
        # remove update.message.chat_id from conversation list
        print "1", e
    except BadRequest as e:
        # handle malformed requests
        print "2", e
    except TimedOut as e:
        # handle slow connection problems
        print "3", e
    except NetworkError as e:
        # handle other connection problems
        print "4", e
    except TelegramError as e:
        # handle all other telegram related errors
        print "6", e 

