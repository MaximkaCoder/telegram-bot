# -*- coding: utf-8 -*-
# !/usr/bin/python3.9
import random
import requests
from datetime import datetime
from datetime import time
import sqlite3
import os
import config
import telebot
from telebot import types

token_number = int(os.environ.get('TOK_NUM'))
# print('TOK_NUM', token_number)

bot = telebot.TeleBot(config.TOKEN[token_number])


admin_max = config.ADMIN_MAX
admin_alina = config.ADMIN_ALINA
admin_vova = config.ADMIN_VOVA
ev = config.EV
am201 = config.SPISOK201
am202 = config.SPISOK202

location = 'Одесса'
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=odessa&appid=5cbeda47b8c5859f4bece2e13a11b5ba"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Погода в городе одесса - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Температура       : {: .0f} °C".format(temp_city))
print("Состояние погоды  :", weather_desc)
print("Влажность         :", hmdt, '%')
print("Скорость ветра    :", wind_spd, 'км/ч')

today = datetime.today()
week = today.strftime("%U")

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("📚Пары📚")
item2 = types.KeyboardButton("🖥Д/З🖥")
item3 = types.KeyboardButton("⌛Звонки⌛")
item = types.KeyboardButton("❗Важные новости❗")
item5 = types.KeyboardButton("📄Лабы📄")
item4 = types.KeyboardButton("ДАЛЕЕ➡")

markup.add(item1, item2, item3, item, item5, item4)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("АМ-201")
item2 = types.KeyboardButton("АМ-202")
item3 = types.KeyboardButton("⬅НАЗАД")
markup2.add(item1, item2, item3)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("ПН")
item2 = types.KeyboardButton("ВТ")
item3 = types.KeyboardButton("СР")
item4 = types.KeyboardButton("ЧТ")
item5 = types.KeyboardButton("ПТ")
item6 = types.KeyboardButton("⬅НАЗАД")
markup3.add(item1, item2, item3, item4, item5, item6)

markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("⬅НАЗАД")
markup4.add(item1)

markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Теория вероятности")
item2 = types.KeyboardButton("Архитектура компьютеров")
item3 = types.KeyboardButton("Системное программирование")
item4 = types.KeyboardButton("ТОЭ")
item5 = types.KeyboardButton("Укр. язык")
item6 = types.KeyboardButton("Психология")
item7 = types.KeyboardButton("Физра")
item8 = types.KeyboardButton("Визуализация информации")
item10 = types.KeyboardButton("Комп. логика")
item9 = types.KeyboardButton("⬅НАЗАД")
markup5.add(item1, item2, item3, item4, item5, item6, item7, item8, item10, item9)

markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("🎲Найти жертву🎲")
item2 = types.KeyboardButton("🙎‍♂Список студентов🙍‍♀")
# item3 = types.KeyboardButton("💼Инфа о преподах💼")
item3 = types.KeyboardButton("📨Розсылка📨")
item4 = types.KeyboardButton("⬅НАЗАД")
item5 = types.KeyboardButton("👥Образовать очередь👥")
item = types.KeyboardButton("☀Погода☀")
ite = types.KeyboardButton("🐶БЕН🐶")
markup6.add(item1, item2, item3, item4, item5, item, ite)

markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Полное расписание 201")
item = types.KeyboardButton("⬅НАЗАД")
markup7.add(item1, item)

markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("АМ201")
item2 = types.KeyboardButton("АМ202")
item3 = types.KeyboardButton("⬅НАЗАД")
markup8.add(item1, item2, item3)

markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Полное расписание 202")
item = types.KeyboardButton("⬅НАЗАД")
markup9.add(item1, item)

markup10 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("201")
item2 = types.KeyboardButton("202")
item3 = types.KeyboardButton("⬅НАЗАД")
markup10.add(item1, item2, item3)

markup11 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item2 = types.KeyboardButton("Я не знаю пароль")
markup11.add(item2)


markup13 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item = types.KeyboardButton("ОТПРАВИТЬ")
item2 = types.KeyboardButton("НЕ ОТПРАВЛЯТЬ")
markup13.add(item, item2)


markup14 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item = types.KeyboardButton("ГОТОВ")
item2 = types.KeyboardButton("НЕ ГОТОВ")
item3 = types.KeyboardButton("ГЕНЕРИРОВАТЬ СПИСОК")
markup14.add(item, item2, item3)


markup15 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item = types.KeyboardButton("РИП")
markup15.add(item)


@bot.message_handler(func=lambda message: message.text == "/start")
def notification(message):
    user_name = message.from_user.username
    user_id = message.from_user.id
    bot.send_message(admin_max, "Пользователь " + str(user_name) + " пытается войти в бота! \nID пользователя - " + str(user_id))
    send_welcome(message)


def send_welcome(message):
    user_id = message.from_user.id
    if str(user_id) in am201 or str(user_id) in am202:
        ui(message)
    else:
        bot.send_message(message.chat.id, "Введите пароль для входа в бота.", reply_markup=markup11)

        bot.register_next_step_handler(message, choise_start)


def choise_start(message):
    global mess
    mess = message.text
    if mess == config.PASSWORD:
        user_name = message.from_user.username
        users_id = message.chat.id
        username = message.from_user.username
        con = sqlite3.connect("my.db")

        cursor = con.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                username text, user_id INT
                           )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS users_201(
                username text, user_id INT
                           )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS users_202(
                username text, user_id INT
                           )""")

        cursor.execute(f"SELECT user_id FROM users WHERE user_id = {users_id}")
        data = cursor.fetchone()

        if data is None:
            cursor.execute('INSERT INTO users VALUES (?, ?)', (username, users_id,))
            con.commit()

        bot.send_message(admin_max, "Пользователь " + str(user_name) + " присоеденился к боту!")
        sti = open('AnimatedSticker.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        username = message.from_user.username
        bot.send_message(message.chat.id, "Ты находишься в главном меню, " + str(username), reply_markup=markup)
    elif mess == "Я не знаю пароль":
        help_pass(message)
    else:
        bot.send_message(message.chat.id, "Пароль не верный!")
        send_welcome(message)


@bot.message_handler(func=lambda message: message.text == "⬅НАЗАД")
def ui(message):
    sti = open('AnimatedSticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    username = message.from_user.username
    text = ['Слава Україні, козаче!', 'А ну скажи паляниця!', 'Хто не скаче - той москаль!', 'Смерть пуйлу!', 'Скільки танків вже вкрав?']
    fraz = random.randint(0, int(len(text)) - 1)
    print(fraz)
    bot.send_message(message.chat.id, text[fraz], reply_markup=markup)


@bot.message_handler(commands=["add"])
def admin(message):
    user_id = message.from_user.id

    if str(user_id) == admin_max:
        message_send_news_news(message)
    else:
        bot.send_message(message.chat.id, "У вас нету прав для выполнения этой комманды!")


def message_send_news_news(message):
    global mess
    mess = message.text
    if mess == "close":
        bot.send_message(message.chat.id, "Сообщение отменено!")
    else:
        bot.send_message(message.chat.id, "Здравствуйте! Отправляйте нужное сообщение!")
        bot.register_next_step_handler(message, reg_message)


def reg_message(message):
    global mess
    mess = message.text
    bot.send_message(message.chat.id, "Сообщение отправлено!", reply_markup=markup)
    file = open('ads.txt', 'a', -1, 'utf-8')
    read = file.write(mess + ' (' + '⏱' + str(datetime.now().date()) + '⏱)\n')
    file.close()

    send(message)


def send(message):
    con = sqlite3.connect("my.db")
    cursor = con.cursor()

    cursor.execute("SELECT user_id FROM users")

    records = cursor.fetchall()

    for us in records:
        try:
            bot.send_message(us[0], "Новое сообщение в разделе ❗Важные новости❗")
        except:
            pass
    con.close()


@bot.message_handler(commands=["news"])
def message_send_news(message):
    bot.send_message(message.chat.id, "Отправляйте нужное сообщение!")
    bot.register_next_step_handler(message, reg_message_news)


def reg_message_news(message):
    global mess
    mess = message.text
    if mess == "close":
        bot.send_message(message.chat.id, "Сообщение отменено!", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Сообщение отправлено!", reply_markup=markup)

        con = sqlite3.connect("my.db")

        cursor = con.cursor()

        cursor.execute("SELECT user_id FROM users")

        records = cursor.fetchall()

        for us in records:
            try:
                sti = open('ben3.webp', 'rb')
                bot.send_sticker(us[0], sti)
                bot.send_message(us[0], mess)
            except:
                pass
        con.close()


@bot.message_handler(func=lambda message: message.text == "❗Важные новости❗" and message.chat.type == 'private')
def news(message):
    file = open('ads.txt', 'r', -1, 'utf-8')

    if os.stat("ads.txt").st_size == 0:
        bot.send_message(message.chat.id, "Тут пока что пусто)", reply_markup=markup)
    else:
        for line in file:
            bot.send_message(message.chat.id, line + '\n', reply_markup=markup)
        file.close()


@bot.message_handler(func=lambda message: message.text == "📨Розсылка📨" and message.chat.type == 'private')
def every_day_sand(message):
    user_id = message.from_user.id
    if str(user_id) == str(admin_max):
        date = datetime.today().isoweekday()
        nums = int(datetime.utcnow().isocalendar()[1])
        nums += 1

        con = sqlite3.connect("my.db")
        cursor = con.cursor()

        cursor.execute("SELECT user_id FROM users")

        records = cursor.fetchall()
        print("I`m started!")
        for us in records:
            try:
                if nums % 2 == 0:
                    print("SEND TO " + str(us[0]))
                    if date == 1:
                        bot.send_message(us[0], "*Нужные ссылки на сегодня:*", parse_mode="Markdown")
                        bot.send_message(us[0], "Языки ООП - https://bit.ly/3a1NLNY\n\n"
                                                "Базы данных - https://bit.ly/3a1NLNY")
                    elif date == 2:
                        bot.send_message(us[0], "*Нужные ссылки на сегодня:*", parse_mode="Markdown")
                        bot.send_message(us[0], "Правознавство - https://cutt.ly/SSaz25n\n\n"
                                                "Конфликтология - https://cutt.ly/bSaxdyT\n\n"
                                                "Политология - https://cutt.ly/ISaxcy6\n\n"
                                                "Языки ООП - https://bit.ly/3a1NLNY\n\n")
                    elif date == 3:
                        bot.send_message(us[0], "Сегодня просто чилим")
                    elif date == 4:
                        bot.send_message(us[0], "*Нужные ссылки на сегодня:*", parse_mode="Markdown")
                        bot.send_message(us[0], "Архитектура компьютеров (АМ201) - https://cutt.ly/IGHeVdh\n\n"
                                                "Архитектура компьютеров (АМ202) - https://cutt.ly/kGHeLS3\n\n"
                                                "Базы данных - https://bit.ly/3a1NLNY")
                    elif date == 5:
                        bot.send_message(us[0], "*Нужные ссылки на сегодня:*", parse_mode="Markdown")
                        bot.send_message(us[0], "Философия - https://cutt.ly/oSalGUT\n\n"
                                                "Архитектура компьютеров - https://cutt.ly/NGHe5Eq")
                else:
                    print("SEND TO " + str(us[0]))
                    if date == 1:
                        bot.send_message(us[0], "*Нужные ссылки на сегодня:*", parse_mode="Markdown")
                        bot.send_message(us[0], "Языки ООП - https://bit.ly/3a1NLNY\n\n"
                                                "Базы данных - https://bit.ly/3a1NLNY")
                    elif date == 2:
                        bot.send_message(us[0], "*Нужные ссылки на сегодня:*", parse_mode="Markdown")
                        bot.send_message(us[0], "Правознавство - https://cutt.ly/SSaz25n\n\n"
                                                "Конфликтология - https://cutt.ly/bSaxdyT\n\n"
                                                "Политология - https://cutt.ly/ISaxcy6\n\n"
                                                "Языки ООП - https://bit.ly/3a1NLNY\n\n"
                                                "Комп. электроника - чилим")
                    elif date == 3:
                        bot.send_message(us[0], "*Нужные ссылки на сегодня:*", parse_mode="Markdown")
                        bot.send_message(us[0], "ТИК - чилим\n\n"
                                                "Комп. электроника - чилим")
                    elif date == 4:
                        bot.send_message(us[0], "*Нужные ссылки на сегодня:*", parse_mode="Markdown")
                        bot.send_message(us[0], "ТИК - чилим\n\n"
                                                "Базы данных - https://bit.ly/3a1NLNY\n\n"
                                                "Философия - https://cutt.ly/oSalGUT")
                    elif date == 5:
                        bot.send_message(us[0], "*Нужные ссылки на сегодня:*", parse_mode="Markdown")
                        bot.send_message(us[0], "Философия - https://cutt.ly/oSalGUT\n\n"
                                                "Архитектура компьютеров - https://cutt.ly/NGHe5Eq")
            except:
                pass
        con.close()
    else:
        bot.send_message(message.chat.id, "У вас нету прав на использование этой функции!")


@bot.message_handler(func=lambda message: message.text == "☀Погода☀" and message.chat.type == 'private')
def weather1(message):
    location = 'Одесса'
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=odessa&appid=5cbeda47b8c5859f4bece2e13a11b5ba"
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    sti = open('sticker3.webp', 'rb')

    if weather_desc == "clear sky":
        weather_desc = "ясно"
        sti = open('AnimatedSticker4.tgs', 'rb')
    elif weather_desc == "broken clouds":
        weather_desc = "переменная облачность"
        sti = open('sticker2.webp', 'rb')
    elif weather_desc == "few clouds":
        weather_desc = "небольшая облачность"
        sti = open('sticker2.webp', 'rb')
    elif weather_desc == "scattered clouds":
        weather_desc = "рассеянные облака"
        sti = open('sticker3.webp', 'rb')
    elif weather_desc == "heavy intensity rain":
        weather_desc = "сильный дождь"
        sti = open('AnimatedSticker2.tgs', 'rb')
    elif weather_desc == "overcast clouds":
        weather_desc = "пасмурно"
        sti = open('AnimatedSticker6.tgs', 'rb')
    elif weather_desc == "light rain":
        weather_desc = "слабый дождь"
        sti = open('AnimatedSticker3.tgs', 'rb')
    elif weather_desc == "moderate rain":
        weather_desc = "умеренный дождь"
        sti = open('AnimatedSticker3.tgs', 'rb')
    round(temp_city)
    bot.send_message(message.chat.id, "Погода в городе ОДЕССА".format(location.upper()), reply_markup=markup6)
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Температура             : {:.0f} °C ".format(temp_city), reply_markup=markup6)
    bot.send_message(message.chat.id, "Состояние погоды  : " + weather_desc, reply_markup=markup6)
    bot.send_message(message.chat.id, "Влажность                 : " + str(hmdt) + "%", reply_markup=markup6)
    bot.send_message(message.chat.id, "Скорость ветра        : " + str(wind_spd) + "км/ч", reply_markup=markup6)


@bot.message_handler(func=lambda message: message.text == "АМ201" and message.chat.type == 'private')
def profilee5(message):
    nums = int(datetime.utcnow().isocalendar()[1])
    print(nums)

    t = time(12, 00, 00).strftime("%H:%M:%S")
    z = datetime.now().strftime("%H:%M:%S")
    print(t)
    print(z)
    if z > t:
        print("zawtra")
    else:
        print("segodnya")

    date = datetime.today().isoweekday()

    if date == 1 and z < t:
        profile(message)
    elif date == 2 and z < t:
        profile1(message, nums)
    elif date == 3 and z < t:
        profile2(message)
    elif date == 4 and z < t:
        profile3(message, nums)
    elif date == 5 and z < t:
        profile4(message, nums)
    elif date == 1 and z > t:
        profile1(message, nums)
    elif date == 2 and z > t:
        profile2(message)
    elif date == 3 and z > t:
        profile3(message, nums)
    elif date == 4 and z > t:
        profile4(message, nums)
    elif date == 5 and z > t:
        profile(message)
    elif date == 6 or date == 7:
        profile(message)


def profile(message):
    bot.send_message(message.chat.id, """<pre>
+---------------------------+
|        ПОНЕДЕЛЬНИК        |
+---------------------+-----+
|          ПАРЫ       | ТИП |
+---------------------+-----+
|1.Теория проэкт. ЭВМ | ЛЕК |
|2.Теория проэкт. ЭВМ | ЛАБ |
|3.Компьютерные сети  | ЛАБ |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")


def profile1(message, nums):
    if (nums % 2) == 0:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ВТОРНИК          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.Вычисл. системы    | ЛАБ |
|2.Выборчая дисц.     | ЛЕК |
|3.СПЗ                | ЛЕК |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ВТОРНИК          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.Пара отсутствует   |  -  |
|2.Выборчая дисц.     | ЛЕК |
|3.Комп. сети         | ЛЕК |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")


def profile2(message):
    bot.send_message(message.chat.id, """<pre>
+----------------------------+
|           СРЕДА            |
+----------------------+-----+
|         ПАРЫ         | ТИП |
+----------------------+-----+
|1.Выборчая дисц.      | ПР  |
|2.СПЗ                 | ЛЕК |
|3.Программ. моб. устр.| ЛЕК |
|4.Пара отсутствует    |  -  |
+----------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")


def profile3(message, nums):
    if (nums % 2) == 0:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ЧЕТВЕРГ          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.СПЗ                | ЛАБ |
|2.Фин. грамотность   | ЛЕК |
|3.Комп. сети         | ЛАБ |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ЧЕТВЕРГ          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.СПЗ                | ЛАБ |
|2.Фин. грамотность   | ЛЕК |
|3.Фин. грамотность   | ПР  |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")


def profile4(message, nums):
    if (nums % 2) == 0:
        bot.send_message(message.chat.id, """<pre>
+----------------------------+
|          ПЯТНИЦА           |
+----------------------+-----+
|         ПАРЫ         | ТИП |
+----------------------+-----+
|1.Программ. моб. устр.| ЛАБ |
|2.Вычисл. системы     | ЛЕК |
|3.Комп. сети          | ЛЕК |
|4.Физра               |  -  |
+----------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ПЯТНИЦА          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.Пара отсутствует   |  -  |
|2.Вычисл. системы    | ЛЕК |
|3.Комп. сети         | ЛЕК |
|4.Физра              |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")


@bot.message_handler(func=lambda message: message.text == "Полное расписание 201")
def timetable(message):
    nums = int(datetime.utcnow().isocalendar()[1])

    profil(message)
    profil1(message, nums)
    profil2(message)
    profil3(message, nums)
    profil4(message, nums)

def profil(message):
    bot.send_message(message.chat.id, """<pre>
+---------------------------+
|        ПОНЕДЕЛЬНИК        |
+---------------------+-----+
|          ПАРЫ       | ТИП |
+---------------------+-----+
|1.Теория проэкт. ЭВМ | ЛЕК |
|2.Теория проэкт. ЭВМ | ЛАБ |
|3.Компьютерные сети  | ЛАБ |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")


def profil1(message, nums):
    if (nums % 2) == 0:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ВТОРНИК          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.Вычисл. системы    | ЛАБ |
|2.Выборчая дисц.     | ЛЕК |
|3.СПЗ                | ЛЕК |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ВТОРНИК          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.Пара отсутствует   |  -  |
|2.Выборчая дисц.     | ЛЕК |
|3.Комп. сети         | ЛЕК |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")


def profil2(message):
    bot.send_message(message.chat.id, """<pre>
+----------------------------+
|           СРЕДА            |
+----------------------+-----+
|         ПАРЫ         | ТИП |
+----------------------+-----+
|1.Выборчая дисц.      | ПР  |
|2.СПЗ                 | ЛЕК |
|3.Программ. моб. устр.| ЛЕК |
|4.Пара отсутствует    |  -  |
+----------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")


def profil3(message, nums):
    if (nums % 2) == 0:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ЧЕТВЕРГ          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.СПЗ                | ЛАБ |
|2.Фин. грамотность   | ЛЕК |
|3.Комп. сети         | ЛАБ |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ЧЕТВЕРГ          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.СПЗ                | ЛАБ |
|2.Фин. грамотность   | ЛЕК |
|3.Фин. грамотность   | ПР  |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")


def profil4(message, nums):
    if (nums % 2) == 0:
        bot.send_message(message.chat.id, """<pre>
+----------------------------+
|          ПЯТНИЦА           |
+----------------------+-----+
|         ПАРЫ         | ТИП |
+----------------------+-----+
|1.Программ. моб. устр.| ЛАБ |
|2.Вычисл. системы     | ЛЕК |
|3.Комп. сети          | ЛЕК |
|4.Физра               |  -  |
+----------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ПЯТНИЦА          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.Пара отсутствует   |  -  |
|2.Вычисл. системы    | ЛЕК |
|3.Комп. сети         | ЛЕК |
|4.Физра              |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup7, parse_mode="HTML")


@bot.message_handler(func=lambda message: message.text == "АМ202" and message.chat.type == 'private')
def profile5(message):
    t = time(12, 00, 00).strftime("%H:%M:%S")
    z = datetime.now().strftime("%H:%M:%S")

    nums = int(datetime.utcnow().isocalendar()[1])
    print(nums)

    print(t)
    print(z)
    if z > t:
        print("zawtra")
    else:
        print("segodnya")

    date = datetime.today().isoweekday()

    if date == 1 and z < t:
        prfile(message)
    elif date == 2 and z < t:
        prfile1(message, nums)
    elif date == 3 and z < t:
        prfile2(message)
    elif date == 4 and z < t:
        prfile3(message, nums)
    elif date == 5 and z < t:
        prfile4(message, nums)
    elif date == 1 and z > t:
        prfile1(message, nums)
    elif date == 2 and z > t:
        prfile2(message)
    elif date == 3 and z > t:
        prfile3(message, nums)
    elif date == 4 and z > t:
        prfile4(message, nums)
    elif date == 5 and z > t:
        prfile(message)
    elif date == 6 or date == 7:
        prfile(message)


def prfile(message):
    bot.send_message(message.chat.id, "*ПОНЕДЕЛЬНИК*", reply_markup=markup7, parse_mode="Markdown")
    bot.send_message(message.chat.id, "1.Теория проэкт. ЭВМ    | ЛЕК.\n\n"
                                      "2.Компьютерные сети   | ЛАБ.\n\n"
                                      "3.Теория проэкт. ЭВМ   | ЛАБ.\n\n"
                                      "4.Пара отсутствует")


def prfile1(message, nums):
    bot.send_message(message.chat.id, "*ВТОРНИК*", reply_markup=markup7, parse_mode="Markdown")

    if (nums % 2) == 0:
        bot.send_message(message.chat.id, "1.Пара отсутствует\n\n"
                                          "2.Выборчая дисц.   | ЛЕК.\n\n"
                                          "3.СПЗ                      | ЛЕК.\n\n"
                                          "4.Пара отсутствует")
    else:
        bot.send_message(message.chat.id, "1.Вычисл. системы  | ЛАБ.\n\n"
                                          "2.Выборчая дисц.   | ЛЕК.\n\n"
                                          "3.Комп. сети           | ЛЕК.\n\n"
                                          "4.Пара отсутствует")


def prfile2(message):
    bot.send_message(message.chat.id, "*СРЕДА*", reply_markup=markup7, parse_mode="Markdown")
    bot.send_message(message.chat.id, "1.Выборчая дисц.           | ПР.\n\n"
                                      "2.СПЗ                             | ЛЕК.\n\n"
                                      "3.Программ. моб. устр. | ЛЕК.\n\n"
                                      "4.Пара отсутствует")


def prfile3(message, nums):
    bot.send_message(message.chat.id, "*ЧЕТВЕРГ*", reply_markup=markup7, parse_mode="Markdown")
    if (nums % 2) == 0:
        bot.send_message(message.chat.id, "1.Пара отсутствует\n\n"
                                          "2.Фин. грамотность  | ЛЕК.\n\n"
                                          "3.Фин. грамотность  | ПР.\n\n"
                                          "4.СПЗ                         | ЛАБ.")
    else:
        bot.send_message(message.chat.id, "1.СПЗ                         | ЛАБ.\n\n"
                                          "2.Фин. грамотность  | ЛЕК.\n\n"
                                          "3.Комп. сети             | ЛАБ.\n\n"
                                          "4.СПЗ                         | ЛАБ.")


def prfile4(message, nums):
    bot.send_message(message.chat.id, "*ПЯТНИЦА*", reply_markup=markup7, parse_mode="Markdown")
    if (nums % 2) == 0:
        bot.send_message(message.chat.id, "1.Пара отсутствует\n\n"
                                          "2.Вычисл. системы       | ЛЕК.\n\n"
                                          "3.Комп. сети                 | ЛЕК.\n\n"
                                          "4.Физра")
    else:
        bot.send_message(message.chat.id, "1.Программ. моб. устр. | ЛАБ\n\n"
                                          "2.Вычисл. системы    | ЛЕК.\n\n"
                                          "3.Комп. сети              | ЛЕК.\n\n"
                                          "4.Физра")

@bot.message_handler(func=lambda message: message.text == "Полное расписание 202")
def timetable(message):
    prfil(message)
    prfil1(message, nums)
    prfil2(message)
    prfil3(message, nums)
    prfil4(message, nums)


def prfil(message):
    bot.send_message(message.chat.id, "*ПОНЕДЕЛЬНИК*", reply_markup=markup7, parse_mode="Markdown")
    bot.send_message(message.chat.id, "1.Теория проэкт. ЭВМ    | ЛЕК.\n\n"
                                      "2.Компьютерные сети   | ЛАБ.\n\n"
                                      "3.Теория проэкт. ЭВМ   | ЛАБ.\n\n"
                                      "4.Пара отсутствует")


def prfil1(message, nums):
    bot.send_message(message.chat.id, "*ВТОРНИК*", reply_markup=markup7, parse_mode="Markdown")

    if (nums % 2) == 0:
        bot.send_message(message.chat.id, "1.Пара отсутствует\n\n"
                                          "2.Выборчая дисц.   | ЛЕК.\n\n"
                                          "3.СПЗ                      | ЛЕК.\n\n"
                                          "4.Пара отсутствует")
    else:
        bot.send_message(message.chat.id, "1.Вычисл. системы  | ЛАБ.\n\n"
                                          "2.Выборчая дисц.   | ЛЕК.\n\n"
                                          "3.Комп. сети           | ЛЕК.\n\n"
                                          "4.Пара отсутствует")


def prfil2(message):
    bot.send_message(message.chat.id, "*СРЕДА*", reply_markup=markup7, parse_mode="Markdown")
    bot.send_message(message.chat.id, "1.Выборчая дисц.           | ПР.\n\n"
                                      "2.СПЗ                             | ЛЕК.\n\n"
                                      "3.Программ. моб. устр. | ЛЕК.\n\n"
                                      "4.Пара отсутствует")


def prfil3(message, nums):
    bot.send_message(message.chat.id, "*ЧЕТВЕРГ*", reply_markup=markup7, parse_mode="Markdown")
    if (nums % 2) == 0:
        bot.send_message(message.chat.id, "1.Пара отсутствует\n\n"
                                          "2.Фин. грамотность  | ЛЕК.\n\n"
                                          "3.Фин. грамотность  | ПР.\n\n"
                                          "4.СПЗ                         | ЛАБ.")
    else:
        bot.send_message(message.chat.id, "1.СПЗ                         | ЛАБ.\n\n"
                                          "2.Фин. грамотность  | ЛЕК.\n\n"
                                          "3.Комп. сети             | ЛАБ.\n\n"
                                          "4.СПЗ                         | ЛАБ.")


def prfil4(message, nums):
    bot.send_message(message.chat.id, "*ПЯТНИЦА*", reply_markup=markup7, parse_mode="Markdown")
    if (nums % 2) == 0:
        bot.send_message(message.chat.id, "1.Пара отсутствует\n\n"
                                          "2.Вычисл. системы       | ЛЕК.\n\n"
                                          "3.Комп. сети                 | ЛЕК.\n\n"
                                          "4.Физра")
    else:
        bot.send_message(message.chat.id, "1.Программ. моб. устр. | ЛАБ\n\n"
                                          "2.Вычисл. системы    | ЛЕК.\n\n"
                                          "3.Комп. сети              | ЛЕК.\n\n"
                                          "4.Физра")


@bot.message_handler(func=lambda message: message.text == "📚Пары📚" and message.chat.type == 'private')
def par(message):
    user_id = message.from_user.id
    for i in am201:
        if str(user_id) == i:
            profilee5(message)

    for i in am202:
        if str(user_id) == i:
            profile5(message)


@bot.message_handler(func=lambda message: message.text == "🎲Найти жертву🎲" and message.chat.type == 'private')
def profile6(message):
    rand = ["Авдеенко Александр Олегович", "Арутюнов Артём Артурович", "Бельчик Кирилл Борисович",
            "Демиденко Никита Александрович", "Емец Андрей Витальевич", "Михайленко Дмитрий Вячеславович",
            "Михайленко Сергей Вячеславович", "Михов Андрей Игоревич", "Орлов Роман Георгиевич",
            "Свобода Тимур Юрьевич", "Смаль Максим Анатольевич", "Черных Кирилл Михайлович", "Чумак Максим Алексеевич",
            "Яковенко Дмитрий Викторович", "Денисюк Диана Александровна"]
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, random.SystemRandom().choice(rand))


@bot.message_handler(func=lambda message: message.text == "🙎‍♂Список студентов🙍‍♀" and message.chat.type == 'private')
def profile7(message):
    bot.send_message(message.chat.id, "Выбери группу студентов!", reply_markup=markup2)


@bot.message_handler(func=lambda message: message.text == "ДАЛЕЕ➡" and message.chat.type == 'private')
def profile8(message):
    bot.send_message(message.chat.id, "Дополнительное меню", reply_markup=markup6)


@bot.message_handler(func=lambda message: message.text == "⌛Звонки⌛" and message.chat.type == 'private')
def profile9(message):
    bot.send_message(message.chat.id, "Смотри не опоздай😉", reply_markup=markup)
    bot.send_message(message.chat.id, "1    8:00-8:45	             8:50-9:35\n", reply_markup=markup)
    bot.send_message(message.chat.id, "2    9:50-10:35	          10:40-11:25\n", reply_markup=markup)
    bot.send_message(message.chat.id, "3    11:40-12:25	        12:30-13:15\n", reply_markup=markup)
    bot.send_message(message.chat.id, "4    13:30-14:15	        14:20-15:05\n", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "АМ-201" and message.chat.type == 'private')
def stud(message):
    bot.send_message(message.chat.id, "Список группы АМ-201: \n", reply_markup=markup2)
    bot.send_message(message.chat.id, "1 Авдеенко Александр Олегович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "2 Арутюнов Артём Артурович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "3 Бельчик Кирилл Борисович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "4 Демиденко Никита Александрович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "5 Емец Андрей Витальевич\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "6 Михайленко Дмитрий Вячеславович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "7 Михайленко Сергей Вячеславович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "8 Михов Андрей Игоревич\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "9 Орлов Роман Георгиевич\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "10 Свобода Тимур Юрьевич\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "11 Смаль Максим Анатольевич\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "12 Черных Кирилл Михайлович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "13 Чумак Максим Алексеевич\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "14 Яковенко Дмитрий Викторович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "15 Денисюк Диана Александровна\n", reply_markup=markup2)


@bot.message_handler(func=lambda message: message.text == "АМ-202" and message.chat.type == 'private')
def stud1(message):
    bot.send_message(message.chat.id, "Список группы АМ-202: \n", reply_markup=markup2)
    bot.send_message(message.chat.id, "1 Безуглая Алина Игорьевна\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "2 Гаврилов Никита Дмитриевич\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "3 Димитров Александр Марчелович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "4 Кочков Роман Борисович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "5 Криворученко Андрей Александрович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "6 Куруч Никита Владимирович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "7 Савченко Денис Вадимович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "8 Сакал Тимофей Юрьевич\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "9 Янчук Владимир Александрович\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "10 Ексаров Павел \n", reply_markup=markup2)
    bot.send_message(message.chat.id, "11 Федчук Евген \n", reply_markup=markup2)
    bot.send_message(message.chat.id, "12 Серооченко Никита \n", reply_markup=markup2)
    bot.send_message(message.chat.id, "13 Бондаренко Илья\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "14 Стадник Константин\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "15 Шостак Ярослав\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "16 Тарасенко Андрей \n", reply_markup=markup2)
    bot.send_message(message.chat.id, "17 Бабич Константин\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "18 Ткачёва Татьяна\n", reply_markup=markup2)
    bot.send_message(message.chat.id, "19 Сивак Дмитрий\n", reply_markup=markup2)


@bot.message_handler(func=lambda message: message.text == "💼Инфа о преподах💼" and message.chat.type == 'private')
def profile10(message):
    bot.send_message(message.chat.id, "Выбери предмет! \n", reply_markup=markup5)


@bot.message_handler(commands=["add_dz_201"])
def admin_201(message):
    user_id = message.from_user.id

    if str(user_id) == admin_max:
        message_send_dz(message)
    else:
        bot.send_message(message.chat.id, "У вас нету прав для выполнения этой комманды!")


def message_send_dz(message):
    bot.send_message(message.chat.id, "Здравствуйте! Отправляйте ДЗ и при этом указывайте предмет!")
    bot.send_message(message.chat.id, "Для отмены напишите close")
    bot.register_next_step_handler(message, reg_message1)


def reg_message1(message):
    global mess
    mess = message.text
    if mess == "close":
        bot.send_message(message.chat.id, "Сообщение отменено!", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Сообщение отправлено!", reply_markup=markup)
        file = open('dz201.txt', 'a', -1, 'utf-8')
        read = file.write(mess + ' (' + '⏱' + str(datetime.now().date()) + '⏱)\n')
        file.close()

        send_dz(message)


def send_dz(message):
    con = sqlite3.connect("my.db")
    cursor = con.cursor()

    cursor.execute("SELECT user_id FROM users_201")

    records = cursor.fetchall()

    for us in records:
        try:
            bot.send_message(us[0], "Новое сообщение в разделе 🖥Д/З🖥")
        except:
            pass
    con.close()


@bot.message_handler(commands=["add_dz_202"])
def admin_202(message):
    user_id = message.from_user.id

    if str(user_id) == admin_max or str(user_id) == admin_alina or str(user_id) == admin_vova:
        message_send_dz_202(message)
    else:
        bot.send_message(message.chat.id, "У вас нету прав для выполнения этой комманды!")


def message_send_dz_202(message):
    bot.send_message(message.chat.id, "Здравствуйте! Отправляйте ДЗ и при этом указывайте предмет!")
    bot.send_message(message.chat.id, "Для отмены напишите close")
    bot.register_next_step_handler(message, reg_message_202)


def reg_message_202(message):
    global mess
    mess = message.text
    if mess == "close":
        bot.send_message(message.chat.id, "Сообщение отменено!", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Сообщение отправлено!", reply_markup=markup)
        file = open('dz202.txt', 'a', -1, 'utf-8')
        read = file.write(mess + ' (' + '⏱' + str(datetime.now().date()) + '⏱)\n')
        file.close()

        send_dz_202(message)


def send_dz_202(message):
    con = sqlite3.connect("my.db")
    cursor = con.cursor()

    cursor.execute("SELECT user_id FROM users_202")

    records = cursor.fetchall()

    for us in records:
        try:
            bot.send_message(us[0], "Новое сообщение в разделе 🖥Д/З🖥")
        except:
            pass
    con.close()


@bot.message_handler(commands=["teacher"])
def send_to_teacher(message):
    #bot.send_message(1772143638, "Напишите комманду /admin_send и напишите ваше имя и отчество. Спасибо за понимание.")
    bot.send_message(1772143638, "Сорян но тяночек не пускаем, этот бот для учёбы.")


@bot.message_handler(commands=["admin_send"])
def send_to_admin1(message):
    # user_id = message.from_user.id
    # if str(user_id) == ev:
    bot.send_message(message.chat.id, "Напишите Ваше имя и отчество (одним сообщением)")
    bot.register_next_step_handler(message, reg_teacher1)
    # else:
    # bot.send_message(message.chat.id, "У вас нету прав для выполнения этой комманды!")


def reg_teacher1(message):
    username = message.from_user.username
    global mess
    mess = message.text + " from " + username
    bot.send_message(message.chat.id, "Сообщение отправлено!", reply_markup=markup11)
    bot.send_message(admin_max, mess)


@bot.message_handler(commands=["admin"])
def send_to_admin(message):
    # user_id = message.from_user.id
    # if str(user_id) == ev:
    bot.send_message(message.chat.id, "Напишите Ваше имя и отчество (одним сообщением)")
    bot.register_next_step_handler(message, reg_teacher)
    # else:
    # bot.send_message(message.chat.id, "У вас нету прав для выполнения этой комманды!")


def reg_teacher(message):
    username = message.from_user.username
    global mess
    mess = message.text + " from " + username
    bot.send_message(message.chat.id, "Сообщение отправлено!", reply_markup=markup)
    bot.send_message(admin_max, mess)


@bot.message_handler(func=lambda message: message.text == "Я не знаю пароль" and message.chat.type == 'private')
def help_pass(message):
    bot.send_message(message.chat.id, "Свяжитесь с админом, для получения пароля.", reply_markup=markup11)
    send_to_admin_mess(message)

def send_to_admin_mess(message):
    bot.send_message(message.chat.id, "Напишите Ваше сообщение админу")
    bot.register_next_step_handler(message, reg_mess_admin)

def reg_mess_admin(message):
    global mess
    mess = message.text
    user_name = message.from_user.username
    bot.send_message(message.chat.id, "Сообщение отправлено!", reply_markup=markup11)
    bot.send_message(admin_max, "Запрос на получение пароля" + " от: " + str(user_name) + "\n" + mess, reply_markup=markup13)
    send_welcome(message)


@bot.message_handler(func=lambda message: message.text == "ОТПРАВИТЬ" and message.chat.type == 'private')
def solution(message):
    bot.send_message(message.chat.id, "Укажите id получателя.")
    bot.register_next_step_handler(message, solution_send)


def solution_send(message):
    global mess
    mess = message.text
    bot.send_message(message.chat.id, "Пользователю открыт доступ!", reply_markup=markup)
    bot.send_message(mess, "Доступ открыт! \n Пароль: QWERTY20X", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "НЕ ОТПРАВЛЯТЬ" and message.chat.type == 'private')
def solution2(message):
    bot.send_message(message.chat.id, "Укажите id получателя.")
    bot.register_next_step_handler(message, solution_no_send)


def solution_no_send(message):
    global mess
    mess = message.text
    bot.send_message(message.chat.id, "Пользователю отказано в доступе!", reply_markup=markup)
    bot.send_message(mess, "Доступ закрыт!", reply_markup=markup15)


@bot.message_handler(func=lambda message: message.text == "201" and message.chat.type == 'private')
def dz_201(message):
    file = open('dz201.txt', 'r', -1, 'utf-8')

    if os.stat("dz201.txt").st_size == 0:
        bot.send_message(message.chat.id, "Тут пока что пусто)", reply_markup=markup4)
    else:
        for line in file:
            bot.send_message(message.chat.id, line + '\n', reply_markup=markup4)
        file.close()


@bot.message_handler(func=lambda message: message.text == "202" and message.chat.type == 'private')
def dz_201(message):
    file = open('dz202.txt', 'r', -1, 'utf-8')

    if os.stat("dz202.txt").st_size == 0:
        bot.send_message(message.chat.id, "Тут пока что пусто)", reply_markup=markup4)
    else:
        for line in file:
            bot.send_message(message.chat.id, line + '\n', reply_markup=markup4)
        file.close()


@bot.message_handler(func=lambda message: message.text == "🖥Д/З🖥" and message.chat.type == 'private')
def dz(message):
    bot.send_message(message.chat.id, "Выбери свою группу", reply_markup=markup10)


@bot.message_handler(func=lambda message: message.text == "📄Лабы📄" and message.chat.type == 'private')
def lab(message):
    bot.send_message(message.chat.id, "Перейдя по ссылке ты увидишь лабы по предметам.", reply_markup=markup)
    bot.send_message(message.chat.id, "https://bit.ly/3kwxJ4F", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Теория вероятности" and message.chat.type == 'private')
def profile12(message):
    bot.send_photo(message.chat.id,
                   "https://op.edu.ua/sites/default/files/styles/staffphoto/public/images/staff/photos/tostanovska-irina-borisivna.jpg?itok=JtjrIvnw")
    bot.send_message(message.chat.id, "Тостановская Ирина Борисовна \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Место обитания - кафедра вышмата \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Электронная почта - tostanovska@op.edu.ua \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Номер телефона - неизвестен \n", reply_markup=markup5)


@bot.message_handler(func=lambda message: message.text == "АМ-201" and message.chat.type == 'private')
def profile13(message):
    bot.send_message(message.chat.id, "Выбери предмет!", reply_markup=markup5)


@bot.message_handler(func=lambda message: message.text == "👥Образовать очередь👥" and message.chat.type == 'private')
def lab_send(message):
    bot.send_message(message.chat.id, "Готов ли ты сдавать лабу?", reply_markup=markup14)


@bot.message_handler(func=lambda message: message.text == "ГОТОВ" and message.chat.type == 'private')
def lab_send(message):
    username = message.from_user.username
    file = open("stack.txt", "r", -1, "utf-8")

    text = file.read()
    if username in text:
        bot.send_message(message.chat.id, "Ты уже есть в списке!)", reply_markup=markup)
        print("bad")
    else:
        file1 = open("stack.txt", 'a', -1, 'utf-8')
        bot.send_message(message.chat.id, "Ты внесён в список.", reply_markup=markup)
        file1.write(str(username) + ' ')
        print("super")


@bot.message_handler(func=lambda message: message.text == "НЕ ГОТОВ" and message.chat.type == 'private')
def lab_send_not(message):
    file1 = open("stack2.txt", "r", -1, "utf-8")
    username = message.from_user.username
    text = file1.read()
    if username in text:
        bot.send_message(message.chat.id, " Я уже понял что ты не будешь сдавать)", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Будь готов на слудующий раз", reply_markup=markup)
        file = open("stack2.txt", "a", -1, "utf-8")
        file.write(str(username) + ' ')


@bot.message_handler(func=lambda message: message.text == "ГЕНЕРИРОВАТЬ СПИСОК" and message.chat.type == 'private')
def lab_send(message):
    user_id = message.from_user.id
    if str(user_id) == admin_max:
        file = open("stack.txt", "r", -1, "utf-8")
        if os.stat("stack.txt").st_size == 0:
            bot.send_message(message.chat.id, "Список пуст!", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Список готов!", reply_markup=markup)
            spisok = []

            for line in file.read().split():
                spisok += line.split()
            print(spisok)

            random.shuffle(spisok)

            con = sqlite3.connect("my.db")
            cursor = con.cursor()

            cursor.execute("SELECT user_id FROM users")

            records = cursor.fetchall()

            for us in records:
                try:
                    bot.send_message(us[0], str(spisok))
                except:
                    pass
            con.close()


        file.close()
    else:
        bot.send_message(message.chat.id, "У вас нету прав на использование этой команды.", reply_markup=markup)



@bot.message_handler(func=lambda message: message.text == "Комп. логика" and message.chat.type == 'private')
def profile14(message):
    bot.send_photo(message.chat.id,
                   "https://opu.ua/sites/default/files/styles/staffphoto/public/images/staff/photos/shaporin-ruslan-olegovych.jpg?itok=KTFWcdDv")
    bot.send_message(message.chat.id, "Шапорин Руслан Олегович \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Место обитания - 812 кабинет \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Электронная почта - shaporin@op.edu.ua \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Номер телефона - +380487058322 \n", reply_markup=markup5)

    bot.send_photo(message.chat.id,
                   "https://op.edu.ua/sites/default/files/styles/staffphoto/public/images/staff/photos/podliegaiev-mihaylo-mikolayovich.jpg?itok=13YFb_sG")
    bot.send_message(message.chat.id, "Подлегаев Михаил Николаевич \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Место обитания - 810 кабинет \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Электронная почта - cuppmm@op.edu.ua \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Номер телефона - неизвестен \n", reply_markup=markup5)


@bot.message_handler(func=lambda message: message.text == "Архитектура компьютеров" and message.chat.type == 'private')
def profile15(message):
    bot.send_photo(message.chat.id,
                   "https://opu.ua/sites/default/files/styles/staffphoto/public/images/staff/photos/blinov-igor-pavlovych.jpg?itok=VFe0xkUz")
    bot.send_message(message.chat.id, "Блинов Игорь Павлович \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Место обитания - 812 кабинет \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Электронная почта - blinov@op.edu.ua \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Номер телефона - неизвестен \n", reply_markup=markup5)


@bot.message_handler(func=lambda message: message.text == "Укр. язык" and message.chat.type == 'private')
def profile16(message):
    bot.send_photo(message.chat.id,
                   "https://op.edu.ua/sites/default/files/styles/staffphoto/public/images/staff/photos/braychenko-svitlana-leonidivna.jpg?itok=6kIZZSnf")
    bot.send_message(message.chat.id, "Брайченко Светлана Леонидовна \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Место обитания - 119Х \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Электронная почта - braychenkosveta@op.edu.ua \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Номер телефона - неизвестен \n", reply_markup=markup5)


@bot.message_handler(
    func=lambda message: message.text == "Системное программирование" and message.chat.type == 'private')
def profile16(message):
    bot.send_message(message.chat.id, "Фото - отсутствует")
    bot.send_message(message.chat.id, "Головачова Елена Викторовна \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Место обитания - 810 кабинет \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Электронная почта - holovachova@op.edu.ua \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Номер телефона - неизвестен \n", reply_markup=markup5)


@bot.message_handler(func=lambda message: message.text == "ТОЭ" and message.chat.type == 'private')
def profile17(message):
    bot.send_photo(message.chat.id,
                   "https://op.edu.ua/sites/default/files/styles/staffphoto/public/images/staff/photos/yarmolovich-viktoriya-yaroslavivna.jpg?itok=RWfa6mUy")
    bot.send_message(message.chat.id, "Ярмолович Виктория Ярославовна \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Место обитания - корпус У \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Электронная почта - yarmolovych@op.edu.ua \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Номер телефона - неизвестен \n", reply_markup=markup5)


@bot.message_handler(func=lambda message: message.text == "Психология" and message.chat.type == 'private')
def profile18(message):
    bot.send_photo(message.chat.id,
                   "https://op.edu.ua/sites/default/files/styles/staffphoto/public/images/staff/photos/todorceva-yuliya-viktorivna.jpg?itok=ZyZ0ruo5")
    bot.send_message(message.chat.id, "Тодорцова Юлия Викторовна \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Место обитания - кафедра психологии \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Электронная почта - todortseva@op.edu.ua \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Номер телефона - +380676018517 \n", reply_markup=markup5)

    bot.send_message(message.chat.id, "Фото - отсутствует")
    bot.send_message(message.chat.id, "Волошенко Марина Олександровна \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Место обитания - 122Х \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Электронная почта - voloshenko@op.edu.ua \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Номер телефона - +380506003747 \n", reply_markup=markup5)


@bot.message_handler(func=lambda message: message.text == "Визуализация информации" and message.chat.type == 'private')
def profile19(message):
    bot.send_photo(message.chat.id,
                   "https://op.edu.ua/sites/default/files/styles/staffphoto/public/images/staff/photos/kopitchuk-igor-mikolayovich.jpg?itok=xkN77VO7")
    bot.send_message(message.chat.id, "Копитчук Игорь Николаевич \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Место обитания - 810 кабинет \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Электронная почта - igor.kopytchuk@op.edu.ua \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Номер телефона - неизвестен \n", reply_markup=markup5)


@bot.message_handler(func=lambda message: message.text == "Физра" and message.chat.type == 'private')
def profile20(message):
    bot.send_photo(message.chat.id,
                   "https://op.edu.ua/sites/default/files/styles/staffphoto/public/images/staff/photos/gromakovska-zinayida-petrivna.jpg?itok=XA-FZxSs")
    bot.send_message(message.chat.id, "Громаковская Зинаида Петровна \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Место обитания - физкорпус \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Электронная почта - z.p.gromakovskaya@op.edu.ua \n", reply_markup=markup5)
    bot.send_message(message.chat.id, "Номер телефона - неизвестен \n", reply_markup=markup5)


@bot.message_handler(func=lambda message: message.text == "🐶БЕН🐶" and message.chat.type == 'private')
def profile21(message):
    sti = open('ben4.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Ben is listening")

    @bot.message_handler(content_types=["text"])
    def ben(message):
        sti = open('ben.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        talks = ['Hohoho', 'Yes', 'No', 'Ughh']
        bot.send_message(message.chat.id, random.choice(talks))


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
