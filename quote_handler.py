# -*- coding: utf-8 -*-
import numpy as np
from telegram import (ForceReply, InlineKeyboardMarkup, InlineKeyboardButton,
                      Chat)
import redis


class Quote:
    def __init__(self, text, msg_id, submitter):
        self.text = text
        self.msg_id = msg_id
        self.submitter = submitter
        self.upvotes = 0
        self.upvoters_id = []


class QuoteHandler:
    """Helper class to handle storage and retrieval of quotes via Telegram"""

    def __init__(self):
        self.db = redis.StrictRedis(db=1)
        self.cur_authors = [] # list of tuples (user_id, prompt_msg_id)
        self.cur_quotes = [] # list of Quote objects (quotes to be added to db)

    def prompt_user(self, bot, update):
        """Prompt user to tell a quote. It will be added to database if upvoted
        at least three times
        """
        if update.message.chat.type != Chat.GROUP:
            update.message.reply_text(text='We need to be in a group chat to '
                                           'add a new quote!')
            return
        user = update.message.from_user
        prompt_msg = update.message.reply_text(
            text='Ok, %s, tell me your quote!' % user.first_name,
            reply_markup=ForceReply(selective=True))
        self.cur_authors.append((user.id, prompt_msg.message_id))

    def handle_new_quote(self, bot, update):
        """Start the upvoting procedure when a new quote is received"""
        quote_msg = update.message
        author = quote_msg.from_user
        reply_to_msg = quote_msg.reply_to_message
        reply_to_id = reply_to_msg.message_id if reply_to_msg is not None else 0

        if (author.id, reply_to_id) not in self.cur_authors:
            # this is not a quote. do nothing
            return

        self.cur_authors.remove((author.id, reply_to_id))
        q = Quote(text=quote_msg.text,
                  msg_id=quote_msg.message_id,
                  submitter=author)
        self.cur_quotes.append(q)
        thumb_up = u'\U0001F44D'
        b = InlineKeyboardButton(thumb_up + ' 0', callback_data=str(q.msg_id))
        keyboard = InlineKeyboardMarkup([[b]])
        quote_msg.reply_text(
          text='Alright, I need three upvotes to add this quote to my database',
          reply_markup=keyboard)

    def save_quote(self, bot, update):
        """Add quote to db when upvoted three times"""
        query = update.callback_query
        voter = query.from_user
        # retrieve quote
        q = filter(lambda q: q.msg_id == int(query.data), self.cur_quotes)
        if len(q) == 0:
            # could not find this quote. this should never happen
            # TODO log an error
            return
        q = q[0]

        if voter.id == q.submitter.id:
            # authors cannot upvote their own story
            bot.answer_callback_query(
                callback_query_id=query.id,
                text=voter.first_name + ' sei un cogliooooooone')
        elif voter.id in q.upvoters_id:
            bot.answer_callback_query(
                callback_query_id=query.id,
                text=voter.first_name + ' sei un cogliooooooone')
        else:
            q.upvoters_id.append(voter.id)
            q.upvotes += 1
            bot.answer_callback_query(
                callback_query_id=query.id,
                text=voter.first_name + ' upvoted the quote')
            if q.upvotes == 3:
                n_quote = self.db.incr('n_quotes')
                self.db.set(str(n_quote), q.text)
                bot.editMessageText(chat_id=query.message.chat_id,
                                    message_id=query.message.message_id,
                                    text='Quote saved to database')
            else:
                thumb_up = u'\U0001F44D'
                button = InlineKeyboardButton(thumb_up + str(q.upvotes),
                                              callback_data=query.data)
                keyboard = InlineKeyboardMarkup([[button]])
                bot.editMessageText(chat_id=query.message.chat_id,
                                    message_id=query.message.message_id,
                                    text=query.message.text,
                                    reply_markup=keyboard)

    def tell_a_quote(self, bot, update):
	"""Tell a quote"""
        msg = update.message
        n_quotes = self.db.get('n_quotes')
        if not n_quotes:
            text = ("I don't know any quotes yet. "
                    'Teach me one using the /addaquote command!')
            msg.reply_text(text=text)
        else:
            rnd_quote = str(np.random.randint(1, int(n_quotes) + 1))
            q = self.db.get(rnd_quote)
            msg.reply_text(text=q, quote=False)
