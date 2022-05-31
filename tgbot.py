from datetime import datetime

import telebot
from telebot import types

from Exchange_rate import exchange_rate_usd, exchange_rate_euro, exchange_rate_gold
from configure import token

bot = telebot.TeleBot(token)
date = datetime.now().strftime('%d.%m.%Y')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Курс доллара\n USD 💵')
    item2 = types.KeyboardButton('Курс Евро\n EURO 💶')
    item3 = types.KeyboardButton('Цена золота\n  GOLD ⚱')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, f"Здравствуй, {message.from_user.username}!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Курс доллара\n USD 💵':
        usd = exchange_rate_usd(usd='')
        bot.send_message(message.chat.id, f'Курс доллара ЦБ РФ на {date}:\n' + str(usd))

    if message.text == 'Курс Евро\n EURO 💶':
        euro = exchange_rate_euro(euro='')
        bot.send_message(message.chat.id, f'Курс евро ЦБ РФ на {date}:\n' + str(euro))

    if message.text == f'Цена золота\n  GOLD ⚱':
        gold = exchange_rate_gold(gold='')
        bot.send_message(message.chat.id, f'Цена золота на {date}:\n' + str(gold))


bot.polling()
