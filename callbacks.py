# -*- coding: utf-8 -*-

from random import random as rand
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
    msg = ''

    if 'ho sbagliato' in text or 'Ho sbagliato' in text \
            or 'ah no' in text  or 'Ah no' in text:
        msg = 'Sei un cogliooooone'
    elif 'no dai' in text or 'No dai' in text:
        msg = 'no dai geeeerry'

    if msg:
        bot.sendMessage(chat_id=chat_id, text=msg)

    if rand() < 1./200.:
        msg = 'oh raga ma la grigliata è confermata?'
        bot.sendMessage(chat_id=chat_id, text=msg)


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

