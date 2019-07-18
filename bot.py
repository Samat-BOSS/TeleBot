#!/usr/bin/env/ python
import random

import telebot
from telebot import types
from telebot.types import Message

TOKEN = '705216273:AAGcRi8la0fJE4YP4nknhDRsJau84teN3y8'
STICKER_ID= 'CAADAgAD3wgAAgi3GQJy0kRXWYjc5QI'

bot=telebot.TeleBot(TOKEN)


def command_hendler(message: Message):
@bot.message_handler(commands=['start','help'])
@bot.message_handler(commands=['start','help'])
    bot.reply_to(message,'there is no answer(')


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    if 'Good afternoon' in message.text:
        bot.reply_to(message,'Good afternoon man!')
        return

    bot.reply_to(message,str(random.random()))

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id,STICKER_ID)

@bot.inline_handler(lambda query: query.query )
def query_text(inline_query):
    try:
        r=types.InlineQueryResultArticle('1','Result',types.InputTextMessageContent('Result message.'))
        r2=types.InlineQueryResultArticle('2','Result',types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id,[r,r2])
    except Exception as e:
        print(e)

bot.polling(timeout=60)



