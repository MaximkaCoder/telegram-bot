# -*- coding: utf-8 -*-
# !/usr/bin/python3.9
import random
import requests
from datetime import datetime
from datetime import time
import datetime as dt
import sqlite3
import os
import config
import telebot
from telebot import types
import multiprocessing
import schedule
import time as tm

token_number = int(os.environ.get('TOK_NUM'))
# print('TOK_NUM', token_number)

bot = telebot.TeleBot(config.TOKEN[token_number])

print(dt.datetime.now())

status_1 = False
status_2 = False
status_3 = False
status_4 = False
status_5 = False

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

today = datetime.today()
week = today.strftime("%U")

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("📚Пары📚")
# item2 = types.KeyboardButton("🎲Найти жертву🎲")
item3 = types.KeyboardButton("⌛Звонки⌛")
item = types.KeyboardButton("☀Погода☀")

# item4 = types.KeyboardButton("ДАЛЕЕ➡")

markup.add(item1, item, item3)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("АМ-201")
item2 = types.KeyboardButton("АМ-202")
markup2.add(item1, item2)

markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("⬅НАЗАД")
markup4.add(item1)

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

markup11 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item2 = types.KeyboardButton("Я не знаю пароль")
markup11.add(item2)

markup13 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item = types.KeyboardButton("ОТПРАВИТЬ")
item2 = types.KeyboardButton("НЕ ОТПРАВЛЯТЬ")
markup13.add(item, item2)


@bot.message_handler(func=lambda message: message.text == "/start")
def notification(message):
    user_name = message.from_user.username
    user_id = message.from_user.id
    bot.send_message(admin_max, "Пользователь " + str(user_name) + " пытается войти в бота! \nID пользователя - " + str(user_id))
    send_welcome(message)


def send_welcome(message):
    user_id = message.from_user.id

    con = sqlite3.connect("my.db")
    cursor = con.cursor()

    cursor.execute(f"SELECT user_id FROM users_201 WHERE user_id = {user_id}")
    data = cursor.fetchone()

    cursor.execute(f"SELECT user_id FROM users_202 WHERE user_id = {user_id}")
    data_2 = cursor.fetchone()

    if str(user_id) in str(data) or str(user_id) in str(data_2):
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

        bot.send_message(message.chat.id, "Из какой ты группы?", reply_markup=markup2)
        bot.register_next_step_handler(message, check_group)
    elif mess == "Я не знаю пароль":
        help_pass(message)
    else:
        bot.send_message(message.chat.id, "Пароль не верный!")
        send_welcome(message)


def check_group(message):
    global mess
    mess = message.text

    users_id = message.chat.id
    username = message.from_user.username

    con = sqlite3.connect("my.db")
    cursor = con.cursor()

    if mess == "АМ-201":
        cursor.execute(f"SELECT user_id FROM users_201 WHERE user_id = {users_id}")
        data = cursor.fetchone()

        if data is None:
            cursor.execute('INSERT INTO users_201 VALUES (?, ?)', (username, users_id,))
            con.commit()
    elif mess == "АМ-202":
        cursor.execute(f"SELECT user_id FROM users_202 WHERE user_id = {users_id}")
        data = cursor.fetchone()

        if data is None:
            cursor.execute('INSERT INTO users_202 VALUES (?, ?)', (username, users_id,))
            con.commit()

    bot.send_message(admin_max, "Пользователь " + str(username) + " присоеденился к боту!")
    bot.send_message(message.chat.id, "Ты находишься в главном меню, " + str(username), reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "⬅НАЗАД")
def ui(message):
    sti = open('AnimatedSticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    text = ['Слава Україні, козаче!', 'А ну скажи паляниця!', 'Хто не скаче - той москаль!', 'Смерть пуйлу!', 'Скільки танків вже вкрав?']
    fraz = random.randint(0, int(len(text)) - 1)
    print(fraz)
    bot.send_message(message.chat.id, text[fraz], reply_markup=markup)


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


@bot.message_handler(func=lambda message: message.text == "☀Погода☀" and message.chat.type == 'private')
def weather1(message):
    location = 'Одесса'
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=odessa&appid=5cbeda47b8c5859f4bece2e13a11b5ba&lang=ru"
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']

    round(temp_city)
    bot.send_message(message.chat.id, "Погода в городе ОДЕССА".format(location.upper()), reply_markup=markup)
    bot.send_message(message.chat.id, "Температура              : {:.0f} °C ".format(temp_city), reply_markup=markup)
    bot.send_message(message.chat.id, "Состояние погоды    : " + weather_desc, reply_markup=markup)
    bot.send_message(message.chat.id, "Влажность                 : " + str(hmdt) + "%", reply_markup=markup)
    bot.send_message(message.chat.id, "Скорость ветра         : " + str(wind_spd) + "км/ч", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "АМ201" and message.chat.type == 'private')
def profilee5(message):
    nums = int(datetime.utcnow().isocalendar()[1])

    t = time(9, 00, 00).strftime("%H:%M:%S")
    z = datetime.now().strftime("%H:%M:%S")

    date = datetime.today().isoweekday()

    if (nums % 2) == 0:
        bot.send_message(message.chat.id, "Это парная неделя")
    else:
        bot.send_message(message.chat.id, "Это непарная неделя")

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
    t = time(9, 00, 00).strftime("%H:%M:%S")
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

    if (nums % 2) == 0:
        bot.send_message(message.chat.id, "Это парная неделя")
    else:
        bot.send_message(message.chat.id, "Это непарная неделя")

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
    bot.send_message(message.chat.id, """<pre>
+---------------------------+
|        ПОНЕДЕЛЬНИК        |
+---------------------+-----+
|          ПАРЫ       | ТИП |
+---------------------+-----+
|1.Теория проэкт. ЭВМ | ЛЕК |
|2.Компьютерные сети  | ЛАБ |
|3.Теория проэкт. ЭВМ | ЛАБ |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup9, parse_mode="HTML")


def prfile1(message, nums):
    bot.send_message(message.chat.id, "*ВТОРНИК*", reply_markup=markup7, parse_mode="Markdown")

    if (nums % 2) == 0:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ВТОРНИК          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.Пара отсутствует   |  -  |
|2.Выборчая дисц.     | ЛЕК |
|3.СПЗ                | ЛЕК |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup9, parse_mode="HTML")

    else:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ВТОРНИК          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.Вычисл. системы    | ЛАБ |
|2.Выборчая дисц.     | ЛЕК |
|3.Комп. сети         | ЛЕК |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup9, parse_mode="HTML")


def prfile2(message):
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
</pre>""", reply_markup=markup9, parse_mode="HTML")


def prfile3(message, nums):
    if (nums % 2) == 0:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ЧЕТВЕРГ          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.Пара отсутствует   |  -  |
|2.Фин. грамотность   | ЛЕК |
|3.Фин. грамотность   | ПР  |
|4.СПЗ                | ЛАБ |
+---------------------+-----+
</pre>""", reply_markup=markup9, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ЧЕТВЕРГ          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.СПЗ                | ЛАБ |
|2.Фин. грамотность   | ЛЕК |
|3.Комп. сети         | ЛАБ |
|4.СПЗ                | ЛАБ |
+---------------------+-----+
</pre>""", reply_markup=markup9, parse_mode="HTML")


def prfile4(message, nums):
    if (nums % 2) == 0:
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
</pre>""", reply_markup=markup9, parse_mode="HTML")
    else:
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
+---------------------+-----+
</pre>""", reply_markup=markup9, parse_mode="HTML")


@bot.message_handler(func=lambda message: message.text == "Полное расписание 202")
def timetable(message):
    nums = int(datetime.utcnow().isocalendar()[1])

    prfil(message)
    prfil1(message, nums)
    prfil2(message)
    prfil3(message, nums)
    prfil4(message, nums)


def prfil(message):
    bot.send_message(message.chat.id, """<pre>
+---------------------------+
|        ПОНЕДЕЛЬНИК        |
+---------------------+-----+
|          ПАРЫ       | ТИП |
+---------------------+-----+
|1.Теория проэкт. ЭВМ | ЛЕК |
|2.Компьютерные сети  | ЛАБ |
|3.Теория проэкт. ЭВМ | ЛАБ |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup9, parse_mode="HTML")


def prfil1(message, nums):
    bot.send_message(message.chat.id, "*ВТОРНИК*", reply_markup=markup7, parse_mode="Markdown")

    if (nums % 2) == 0:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ВТОРНИК          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.Пара отсутствует   |  -  |
|2.Выборчая дисц.     | ЛЕК |
|3.СПЗ                | ЛЕК |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup9, parse_mode="HTML")

    else:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ВТОРНИК          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.Вычисл. системы    | ЛАБ |
|2.Выборчая дисц.     | ЛЕК |
|3.Комп. сети         | ЛЕК |
|4.Пара отсутствует   |  -  |
+---------------------+-----+
</pre>""", reply_markup=markup9, parse_mode="HTML")


def prfil2(message):
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
</pre>""", reply_markup=markup9, parse_mode="HTML")


def prfil3(message, nums):
    if (nums % 2) == 0:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ЧЕТВЕРГ          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.Пара отсутствует   |  -  |
|2.Фин. грамотность   | ЛЕК |
|3.Фин. грамотность   | ПР  |
|4.СПЗ                | ЛАБ |
+---------------------+-----+
</pre>""", reply_markup=markup9, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ЧЕТВЕРГ          |
+---------------------+-----+
|         ПАРЫ        | ТИП |
+---------------------+-----+
|1.СПЗ                | ЛАБ |
|2.Фин. грамотность   | ЛЕК |
|3.Комп. сети         | ЛАБ |
|4.СПЗ                | ЛАБ |
+---------------------+-----+
</pre>""", reply_markup=markup9, parse_mode="HTML")


def prfil4(message, nums):
    if (nums % 2) == 0:
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
</pre>""", reply_markup=markup9, parse_mode="HTML")
    else:
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
+---------------------+------+
</pre>""", reply_markup=markup9, parse_mode="HTML")


@bot.message_handler(func=lambda message: message.text == "📚Пары📚" and message.chat.type == 'private')
def par(message):
    con = sqlite3.connect("my.db")
    cursor = con.cursor()

    user_id = message.from_user.id

    cursor.execute(f"SELECT user_id FROM users_201 WHERE user_id = {user_id}")
    data = cursor.fetchone()

    if str(user_id) in str(data):
        profilee5(message)

    cursor.execute(f"SELECT user_id FROM users_202 WHERE user_id = {user_id}")
    data = cursor.fetchone()

    if str(user_id) in str(data):
        profile5(message)


    # for i in am201:
        # if str(user_id) == i:
            # profilee5(message)

    # for i in am202:
        # if str(user_id) == i:
            # profile5(message)


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


@bot.message_handler(func=lambda message: message.text == "⌛Звонки⌛" and message.chat.type == 'private')
def profile9(message):
    bot.send_message(message.chat.id, """<pre>
+-----------------------------+
|           ЗВОНКИ            |
+--------------+--------------+
| 1-я полупара | 2-я полупара |        
+--------------+-------+------+
|1. 8:00-8:45  |   8:50-9:35  |
|2. 9:50-10:35 |  10:40-11:25 |
|3.11:40-12:25 |  12:30-13:15 |        
|4.13:30-14:15 |  14:20-15:05 |             
+--------------+--------------+
    </pre>""", reply_markup=markup, parse_mode="HTML")


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


def checking():
    now = dt.datetime.now()
    global status_1, status_2, status_3, status_4, status_5
    nums = int(datetime.utcnow().isocalendar()[1])
    date = datetime.today().isoweekday()

    con = sqlite3.connect("my.db")
    cursor = con.cursor()
    user_id = message.from_user.id

    cursor.execute(f"SELECT user_id FROM users_201 WHERE user_id = {user_id}")
    data_1 = cursor.fetchone()

    cursor.execute(f"SELECT user_id FROM users_202 WHERE user_id = {user_id}")
    data_2 = cursor.fetchone()

    early_par = time.fromisoformat('04:50:00')
    par_1_s = time.fromisoformat('05:00:00')
    par_1_e = time.fromisoformat('06:35:00')

    par_2_s = time.fromisoformat('06:50:00')
    par_2_e = time.fromisoformat('08:25:00')

    par_3_s = time.fromisoformat('08:40:00')
    par_3_e = time.fromisoformat('10:15:00')

    par_4_s = time.fromisoformat('10:30:00')
    par_4_e = time.fromisoformat('12:05:00')
    tm_now = now.time()

    if user_id in data_1:
        if nums % 2 == 0:
            if date == 1:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_max, "Ссылка на Теорию проэктирования ЭВМ\n\nhttps://cutt.ly/lVPEADJ")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_max, "Ссылка на Компьютерные сети\n\nhttps://cutt.ly/dVPEBXb")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_max, "Ссылка на Теорию проэктирования ЭВМ\n\nhttps://cutt.ly/lVPEADJ")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 2:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_max, "Ссылка на Вычислительные системы\n\nhttps://cutt.ly/cVPYhMS")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_max, "Сейчас пара по выборчей дисциплине, сообщите админу (@programuller) о ссылках "
                                     "на другие "
                                     "дисциплины\nСсылка на Эстетику\n\nhttps://cutt.ly/KVSesN4")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_max, "Ссылка на СПЗ\n\nhttps://cutt.ly/3VPR831")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 3:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_max, "Сейчас пара по выборчей дисциплине, сообщите админу (@programuller) о ссылках "
                                     "на другие "
                                     "дисциплины\nСсылка на Эстетику\n\nhttps://cutt.ly/KVSesN4")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_max, "Ссылка на СПЗ\n\nhttps://cutt.ly/3VPR831")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_max, "Ссылка на Программирование мобильных устройств\n\nhttps://cutt.ly/aVPTiqJ")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 4:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_max, "Ссылка на СПЗ\n\nhttps://cutt.ly/3VPR831")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_max, "Ссылка на Финансовую грамотность\n\nhttps://cutt.ly/pVPYwhC")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 5:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_max, "Ссылка на Программирование мобильных устройств\n\nhttps://cutt.ly/aVPTiqJ")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_max, "Ссылка на Вычислительные системы\n\nhttps://cutt.ly/cVPYhMS")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_max, "Ссылка на Компьютерные сети\n\nhttps://cutt.ly/xVPYbnP")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
        else:
            if date == 1:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_max, "Ссылка на Теорию проэктирования ЭВМ\n\nhttps://cutt.ly/lVPEADJ")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_max, "Ссылка на Компьютерные сети\n\nhttps://cutt.ly/dVPEBXb")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_max, "Ссылка на Теорию проэктирования ЭВМ\n\nhttps://cutt.ly/lVPEADJ")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 2:
                if par_1_s > tm_now > early_par and not status_1:
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_max, "Сейчас пара по выборчей дисциплине, сообщите админу (@programuller) о ссылках "
                                     "на другие "
                                     "дисциплины\nСсылка на Эстетику\n\nhttps://cutt.ly/KVSesN4")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_max, "Ссылка на Компьютерные сети\n\nhttps://cutt.ly/fVPRKfC")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 3:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_max, "Сейчас пара по выборчей дисциплине, сообщите админу (@programuller) о ссылках "
                                     "на другие "
                                     "дисциплины\nСсылка на Эстетику\n\nhttps://cutt.ly/KVSesN4")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_max, "Ссылка на СПЗ\n\nhttps://cutt.ly/3VPR831")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_max, "Ссылка на Программирование мобильных устройств\n\nhttps://cutt.ly/aVPTiqJ")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 4:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_max, "Ссылка на СПЗ\n\nhttps://cutt.ly/3VPR831")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_max, "Ссылка на Финансовую грамотность\n\nhttps://cutt.ly/pVPYwhC")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 5:
                if par_1_s > tm_now > early_par and not status_1:
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_max, "Ссылка на Вычислительные системы\n\nhttps://cutt.ly/cVPYhMS")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_max, "Ссылка на Компьютерные сети\n\nhttps://cutt.ly/xVPYbnP")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
    elif user_id in data_2:
        if nums % 2 == 0:
            if date == 1:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_vova, "Ссылка на Теорию проэктирования ЭВМ\n\nhttps://cutt.ly/lVPEADJ")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_vova, "Ссылка на Компьютерные сети\n\nhttps://cutt.ly/dVPEBXb")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_vova, "Ссылка на Теорию проэктирования ЭВМ\n\nhttps://cutt.ly/lVPEADJ")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 2:
                if par_1_s > tm_now > early_par and not status_1:
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_vova,
                                     "Сейчас пара по выборчей дисциплине, сообщите админу (@programuller) о ссылках "
                                     "на другие "
                                     "дисциплины\nСсылка на Эстетику\n\nhttps://cutt.ly/KVSesN4")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_vova, "Ссылка на СПЗ\n\nhttps://cutt.ly/3VPR831")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 3:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_vova,
                                     "Сейчас пара по выборчей дисциплине, сообщите админу (@programuller) о ссылках "
                                     "на другие "
                                     "дисциплины\nСсылка на Эстетику\n\nhttps://cutt.ly/KVSesN4")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_vova, "Ссылка на СПЗ\n\nhttps://cutt.ly/3VPR831")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_vova,
                                     "Ссылка на Программирование мобильных устройств\n\nhttps://cutt.ly/aVPTiqJ")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 4:
                if par_1_s > tm_now > early_par and not status_1:
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_vova, "Ссылка на Финансовую грамотность\n\nhttps://cutt.ly/pVPYwhC")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    bot.send_message(admin_vova, "Ссылка на СПЗ\n\nhttps://cutt.ly/3VPR831")
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 5:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_vova,
                                     "Ссылка на Программирование мобильных устройств\n\nhttps://cutt.ly/aVPTiqJ")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_vova, "Ссылка на Вычислительные системы\n\nhttps://cutt.ly/cVPYhMS")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_vova, "Ссылка на Компьютерные сети\n\nhttps://cutt.ly/xVPYbnP")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
        else:
            if date == 1:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_vova, "Ссылка на Теорию проэктирования ЭВМ\n\nhttps://cutt.ly/lVPEADJ")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_vova, "Ссылка на Компьютерные сети\n\nhttps://cutt.ly/dVPEBXb")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_vova, "Ссылка на Теорию проэктирования ЭВМ\n\nhttps://cutt.ly/lVPEADJ")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 2:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_vova, "Ссылка на Вычислительные системы\n\nhttps://cutt.ly/cVPYhMS")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_vova,
                                     "Сейчас пара по выборчей дисциплине, сообщите админу (@programuller) о ссылках "
                                     "на другие "
                                     "дисциплины\nСсылка на Эстетику\n\nhttps://cutt.ly/KVSesN4")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_vova, "Ссылка на Компьютерные сети\n\nhttps://cutt.ly/fVPRKfC")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 3:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_vova,
                                     "Сейчас пара по выборчей дисциплине, сообщите админу (@programuller) о ссылках "
                                     "на другие "
                                     "дисциплины\nСсылка на Эстетику\n\nhttps://cutt.ly/KVSesN4")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_vova, "Ссылка на СПЗ\n\nhttps://cutt.ly/3VPR831")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_vova,
                                     "Ссылка на Программирование мобильных устройств\n\nhttps://cutt.ly/aVPTiqJ")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 4:
                if par_1_s > tm_now > early_par and not status_1:
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_vova, "Ссылка на Финансовую грамотность\n\nhttps://cutt.ly/pVPYwhC")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    bot.send_message(admin_vova, "Ссылка на СПЗ\n\nhttps://cutt.ly/3VPR831")
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False
            elif date == 5:
                if par_1_s > tm_now > early_par and not status_1:
                    bot.send_message(admin_vova,
                                     "Ссылка на Программирование мобильных устройств\n\nhttps://cutt.ly/aVPTiqJ")
                    status_1 = True
                elif par_2_s > tm_now > par_1_e and not status_2:
                    bot.send_message(admin_vova, "Ссылка на Вычислительные системы\n\nhttps://cutt.ly/cVPYhMS")
                    status_2 = True
                elif par_3_s > tm_now > par_2_e and not status_3:
                    bot.send_message(admin_vova, "Ссылка на Компьютерные сети\n\nhttps://cutt.ly/xVPYbnP")
                    status_3 = True
                elif par_4_s > tm_now > par_3_e and not status_4:
                    status_4 = True
                elif tm_now > par_4_e:
                    status_1 = False
                    status_2 = False
                    status_3 = False
                    status_4 = False


def starting_checking():
    schedule.every(2).minutes.do(checking)

    while True:
        schedule.run_pending()
        tm.sleep(1)


def main():
    p = multiprocessing.Process(target=starting_checking, args=())
    p.start()
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
