import telebot
import requests
import time
from bs4 import BeautifulSoup

token = '1081739813:AAHKtJ0-DbMx8TtOxZ277_tMcd6xTojMTTg'
bot = telebot.TeleBot(token)


# получение новостей в листе
r = requests.get('https://newsapi.org/v2/top-headlines?apiKey=ba88909bbda0454aaa503a8fff5e1225&country=ru')
r_dict = r.json()
r_articles = r_dict['articles']
print(r_articles)


# получение времени в листе
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
ct = current_time.split(':')
print(ct)




@bot.message_handler(commands=['start'])
def say_hello(message):
    # установление клавиатуры и приветствие пользователя
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    b1 = telebot.types.KeyboardButton('Новости')
    b2 = telebot.types.KeyboardButton('Курс валюты')
    user_markup.add(b1, b2)
    bot.send_message(message.from_user.id, 'Welcome to Akimikano news', reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def start_news(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    b1 = telebot.types.KeyboardButton('Новости')
    b2 = telebot.types.KeyboardButton('Курс валюты')
    user_markup.add(b1, b2)
    global r_articles
    flag = True
    if message.text == 'Новости':
        while flag:
            for i in r_articles:
                if int(ct[0]) >= 9:  # итерация начинается если время больше чем 9 часов утра
                    # здесь из каждого элемента листа получаем название, описание и ссылку
                    bot.send_message(message.from_user.id, i['title'] + ' ' + i['description'] + ' ' + i['url'])
                    time.sleep(1800)  # указываем что новости будут отправляться каждые пол часа

            # если итерация доходит по последней новости или время больше 10 часов ночи то отправка останавливается
                elif i == r_articles[20] or int(ct[0]) >= 22:
                    flag = False

        # функция курса валюты
    elif message.text == 'Курс валюты':

        # получение реальных значений с сайта KICB через библиотеку BeautifulSoup
        # и сохранение их в двух листах
        source = requests.get('https://kicb.net/welcome/').text
        soup = BeautifulSoup(source, 'lxml')

        buying = []
        selling = []

        a = soup.find('div', class_='con')
        b = a.find_all('div', class_='cur_line')
        b.remove(b[0])
        for i in b:
            buying1 = i.find('div', class_='data2')
            buying2 = buying1.span.text
            buying.append(buying2)

            selling1 = i.find('div', class_='data3')
            selling2 = selling1.span.text
            selling.append(selling2)
            # отправка значений курса валют
        bot.send_message(message.from_user.id, 'USD buying:' + buying[0] + ' selling:' + selling[0] +
                                                '\nEUR buying:' + buying[1] + ' selling:' + selling[1] +
                                                '\nRUB buying:' + buying[2] + ' selling:' + selling[2] +
                                                '\nKZT buying:' + buying[3] + ' selling:' + selling[3])






































bot.polling(none_stop=True)