import telebot
import requests
import json
import time
from bs4 import BeautifulSoup

token = '1081739813:AAHKtJ0-DbMx8TtOxZ277_tMcd6xTojMTTg'
bot = telebot.TeleBot(token)

r = requests.get('https://newsapi.org/v2/top-headlines?apiKey=ba88909bbda0454aaa503a8fff5e1225&country=ru')
r_dict = r.json()
r_articles = r_dict['articles']
print(r_articles)

# t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
# ct = current_time.split(':')
# print(ct)

r_money = requests.get('https://free.currconv.com/api/v7/convert?q=USD_EUR&compact=ultra&apiKey=fe4202ff43aacf90dd31')
r_money_j = r_money.json()
print(r_money_j['USD_EUR'])


@bot.message_handler(commands=['start'])
def say_hello(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    b1 = telebot.types.KeyboardButton('Новости')
    b2 = telebot.types.KeyboardButton('Курс валюты')
    b3 = telebot.types.KeyboardButton('Погода')
    user_markup.add(b1, b2, b3)
    bot.send_message(message.from_user.id, 'Welcome to Akimikano news', reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def start_news(message):
    global r_articles
    if message.text == 'Новости':
        flag = True
        while flag:
            for i in r_articles[::-1]:
                # if int(ct[0]) >= 9:
                bot.send_message(message.from_user.id, i['title'].upper() + ' ' + i['description'] + ' ' + i['url'])
                time.sleep(5)
                # elif i == r_articles[0] or int(ct[0]) >= 22:
                #     flag = False
    # bot.send_message(message.from_user.id, r_articles[0]['title'])


@bot.message_handler(content_types=['text'])
def money(message):
    global r_money_j
    if message.text == 'Курс валюты':
        bot.send_message(message.from_user.id, r_money_j['USD_EUR'])






































bot.polling(none_stop=True)