# -*- coding: utf-8 -*-
# !/usr/bin/python3.9
import random
from datetime import datetime, time
import sqlite3
import config
import telebot
from telebot import types
import multiprocessing
import time as tm

bot = telebot.TeleBot(config.TOKEN[0])

admin_max = config.ADMIN_MAX
admin_alina = config.ADMIN_ALINA
admin_vova = config.ADMIN_VOVA

PRICE = types.LabeledPrice(label="Підписка на 1 місяць", amount=10*100)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("📒Пари📒")
item2 = types.KeyboardButton("‍🧑‍🎓Студенти🧑‍🎓")
item3 = types.KeyboardButton("🕛Дзвоник🕛")

markup.row(item1, item2)
markup.row(item3)

markup2 = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton("АМ-201", callback_data="1")
btn2 = types.InlineKeyboardButton("АМ-202", callback_data="2")
markup2.add(btn1, btn2)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("АМ-201")
btn2 = types.KeyboardButton("АМ-202")
markup3.add(btn1, btn2)

markup201 = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton("Інша група", callback_data="1")
markup201.add(btn1)

markup202 = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton("Інша група", callback_data="2")
markup202.add(btn1)

markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("⬅НАЗАД")
markup4.add(item1)

markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Відмінити")
markup5.add(item1)

markup7 = types.InlineKeyboardMarkup()
btn4 = types.InlineKeyboardButton("Повний розклад", callback_data="5")
markup7.add(btn4)

markup8 = types.InlineKeyboardMarkup()
btn5 = types.InlineKeyboardButton("Згорнути", callback_data="6")
markup8.add(btn5)

markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Полное расписание 202")
item = types.KeyboardButton("⬅НАЗАД")
markup9.add(item1, item)

markup11 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item2 = types.KeyboardButton("Я не знаю пароль")
markup11.add(item2)

markup13 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item = types.KeyboardButton("Відправити")
item2 = types.KeyboardButton("⬅НАЗАД")
markup13.add(item, item2)


def get_schedule_am_201(day):
    week = datetime.now().isocalendar().week + 1
    if day == "Monday":
        if week % 2 != 0:
            return {
                "06:45": "Міжмашинна взаємодія-https://cutt.ly/H8TIIjF",
                "08:35": "Системи реального часу-https://cutt.ly/4846uYf",
                "10:25": "Системи реального часу-https://cutt.ly/4846uYf"
            }
        else:
            return {
                "06:45": "Міжмашинна взаємодія-https://cutt.ly/H8TIIjF",
                "08:35": "Системи реального часу-https://cutt.ly/4846uYf"
            }

    elif day == "Tuesday":
        if week % 2 != 0:
            return {
                "06:45": "Конфліктологія-https://cutt.ly/G87qYD4",
                "06:46": "Політологія-https://cutt.ly/v87wdvE",
                "08:35": "Системи реального часу-https://cutt.ly/4846uYf",
                "10:25": "Міжмашинна взаємодія-https://cutt.ly/H8TIIjF"
            }
        else:
            return {
                "06:45": "Конфліктологія-https://cutt.ly/187qLhf",
                "06:46": "Політологія-https://cutt.ly/U87wxf2",
                "06:47": "Правове регулювання інформаційної діяльності-https://cutt.ly/J4HGQA8",
                "08:35": "Системи реального часу-https://cutt.ly/4846uYf",
                "10:25": "Теорія проектування ЕОМ-https://cutt.ly/E8EbpjF"
            }
    elif day == "Wednesday":
        return {
            "04:55": "Політологія-https://cutt.ly/v87wdvE",
            "04:56": "Правове регулювання інформаційної діяльності-https://cutt.ly/J4HGQA8",
            "06:45": "Проектування МПС-https://cutt.ly/T8FHVOF"
        }
    elif day == "Thursday":
        if week % 2 != 0:
            return {
                "04:55": "Комп'ютерні системи штучного інтелекту-https://cutt.ly/x8Ev3Lh",
                "06:45": "Проектування МПС-https://cutt.ly/E8FH8CK",
                "08:35": "Системи реального часу-https://cutt.ly/4846uYf"
            }
        else:
            return {
                "04:55": "Комп'ютерні системи штучного інтелекту-https://cutt.ly/x8Ev3Lh",
                "08:45": "Комп'ютерні системи штучного інтелекту-https://cutt.ly/x8Ev3Lh"
            }
    elif day == "Friday":
        return {
            "08:35": "Теорія проектування ЕОМ-https://cutt.ly/E8EbpjF"
        }
    else:
        return {}


def get_schedule_am_202(day):
    week = datetime.now().isocalendar().week + 1
    if day == "Monday":
        if week % 2 != 0:
            return {
                "06:45": "Міжмашинна взаємодія-https://cutt.ly/H8TIIjF",
                "08:35": "Системи реального часу-https://cutt.ly/4846uYf"
            }
        else:
            return {
                "06:45": "Міжмашинна взаємодія-https://cutt.ly/H8TIIjF",
                "08:35": "Системи реального часу-https://cutt.ly/4846uYf",
                "10:25": "Системи реального часу-https://cutt.ly/4846uYf"
            }
    elif day == "Tuesday":
        if week % 2 != 0:
            return {
                "06:45": "Конфліктологія-https://cutt.ly/G87qYD4",
                "06:46": "Політологія-https://cutt.ly/v87wdvE",
                "08:35": "Міжмашинна взаємодія-https://cutt.ly/H8TIIjF",
                "10:25": "Системи реального часу-https://cutt.ly/4846uYf"
            }
        else:
            return {
                "06:45": "Конфліктологія-https://cutt.ly/187qLhf",
                "06:46": "Політологія-https://cutt.ly/U87wxf2",
                "08:35": "Теорія проектування ЕОМ-https://cutt.ly/E8EbpjF",
                "10:25": "Системи реального часу-https://cutt.ly/4846uYf"
            }
    elif day == "Wednesday":
        return {
            "06:45": "Проектування МПС-https://cutt.ly/T8FHVOF"
        }
    elif day == "Thursday":
        if week % 2 != 0:
            return {
                "04:55": "Комп'ютерні системи штучного інтелекту-https://cutt.ly/x8Ev3Lh",
                "06:45": "Комп'ютерні системи штучного інтелекту-https://cutt.ly/x8Ev3Lh",
                "08:35": "Системи реального часу-https://cutt.ly/4846uYf"
            }
        else:
            return {
                "04:55": "Комп'ютерні системи штучного інтелекту-https://cutt.ly/x8Ev3Lh",
                "06:45": "Проектування МПС-https://cutt.ly/e8FH6VR"
            }

    elif day == "Friday":
        return {
            "08:35": "Теорія проектування ЕОМ-https://cutt.ly/E8EbpjF"
        }
    else:
        return {}


am_201_schedule_n_p = {
    1: """<pre>
+---------------------------+
|         ПОНЕДІЛОК         |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Пара відсутня      |  -  |
|2.Міжмаш. взаємодія  | ЛЕК |
|3.Сис. реальн. часу  | ЛЕК |
|4.Сис. реальн. часу  | ЛАБ |
+---------------------+-----+
|      НЕПАРНИЙ ТИЖДЕНЬ     |
+---------------------------+
</pre>""",
    2: """<pre>
+---------------------------+
|          ВІВТОРОК         |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Пара відсутня      |  -  |
|2.Вибіркова дисципл. |  ?  |
|3.Сис. реальн. часу  | ЛАБ |
|4.Міжмаш. взаємодія  | ЛАБ |
+---------------------+-----+
|     НЕПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    3: """<pre>
+---------------------------+
|           СЕРЕДА          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Вибіркова дисципл. |  ?  |
|2.Проектування МПС   | ЛЕК |
|3.Пара відсутня      |  -  |
|4.Пара відсутня      |  -  |
+---------------------+-----+
|     НЕПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    4: """<pre>
+---------------------------+
|           ЧЕТВЕР          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Комп. сис. шт. інт.| ЛЕК |
|2.Проектування МПС   | ЛАБ |
|3.Сис. реальн. часу  | ЛЕК |
|4.Пара відсутня      |  -  |
+---------------------+-----+
|     НЕПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    5: """<pre>
+---------------------------+
|         П'ятниця          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Пара відсутня      |  -  |
|2.Пара відсутня      |  -  |
|3.Теорія проект. ЕОМ | ЛЕК |
|4.Фізичне виховання  |  -  |
+---------------------+-----+
|     НЕПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>"""
}

am_201_schedule_p = {
    1: """<pre>
+---------------------------+
|         ПОНЕДІЛОК         |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Пара відсутня      |  -  |
|2.Міжмаш. взаємодія  | ЛЕК |
|3.Сис. реальн. часу  | ЛЕК |
|4.Пара відсутня      |  -  |
+---------------------+-----+
|       ПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    2: """<pre>
+---------------------------+
|          ВІВТОРОК         |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Пара відсутня      |  -  |
|2.Вибіркова дисципл. |  ?  |
|3.Сис. реальн. часу  | ЛАБ |
|4.Теорія проект. ЕОМ | ЛАБ |
+---------------------+-----+
|       ПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    3: """<pre>
+---------------------------+
|           СЕРЕДА          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Вибіркова дисципл. |  ?  |
|2.Проектування МПС   | ЛЕК |
|3.Пара відсутня      |  -  |
|4.Пара відсутня      |  -  |
+---------------------+-----+
|       ПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    4: """<pre>
+---------------------------+
|           ЧЕТВЕР          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Комп. сис. шт. інт.| ЛЕК |
|2.Комп. сис. шт. інт.| ЛАБ |
|3.Пара відсутня      |  -  |
|4.Пара відсутня      |  -  |
+---------------------+-----+
|       ПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    5: """<pre>
+---------------------------+
|         П'ятниця          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Пара відсутня      |  -  |
|2.Пара відсутня      |  -  |
|3.Теорія проект. ЕОМ | ЛЕК |
|4.Фізичне виховання  |  -  |
+---------------------+-----+
|       ПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>"""
}

am_202_schedule_n_p = {
    1: """<pre>
+---------------------------+
|         ПОНЕДІЛОК         |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Пара відсутня      |  -  |
|2.Міжмаш. взаємодія  | ЛЕК |
|3.Сис. реальн. часу  | ЛЕК |
|4.Пара відсутня      |  -  |
+---------------------+-----+
|      НЕПАРНИЙ ТИЖДЕНЬ     |
+---------------------------+
</pre>""",
    2: """<pre>
+---------------------------+
|          ВІВТОРОК         |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Пара відсутня      |  -  |
|2.Вибіркова дисципл. |  ?  |
|3.Міжмаш. взаємодія  | ЛАБ |
|4.Сис. реальн. часу  | ЛАБ |
+---------------------+-----+
|     НЕПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    3: """<pre>
+---------------------------+
|           СЕРЕДА          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Вибіркова дисципл. |  ?  |
|2.Проектування МПС   | ЛЕК |
|3.Пара відсутня      |  -  |
|4.Пара відсутня      |  -  |
+---------------------+-----+
|     НЕПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    4: """<pre>
+---------------------------+
|           ЧЕТВЕР          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Комп. сис. шт. інт.| ЛЕК |
|2.Комп. сис. шт. інт.| ЛАБ |
|3.Сис. реальн. часу  | ЛЕК |
|4.Пара відсутня      |  -  |
+---------------------+-----+
|     НЕПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    5: """<pre>
+---------------------------+
|         П'ятниця          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Пара відсутня      |  -  |
|2.Пара відсутня      |  -  |
|3.Теорія проект. ЕОМ | ЛЕК |
|4.Фізичне виховання  |  -  |
+---------------------+-----+
|     НЕПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>"""
}

am_202_schedule_p = {
    1: """<pre>
+---------------------------+
|         ПОНЕДІЛОК         |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Пара відсутня      |  -  |
|2.Міжмаш. взаємодія  | ЛЕК |
|3.Сис. реальн. часу  | ЛЕК |
|4.Сис. реальн. часу  | ЛАБ |
+---------------------+-----+
|       ПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    2: """<pre>
+---------------------------+
|          ВІВТОРОК         |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Пара відсутня      |  -  |
|2.Вибіркова дисципл. |  ?  |
|3.Теорія проект. ЕОМ | ЛАБ |
|4.Сис. реальн. часу  | ЛАБ |
+---------------------+-----+
|       ПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    3: """<pre>
+---------------------------+
|           СЕРЕДА          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Вибіркова дисципл. |  ?  |
|2.Проектування МПС   | ЛЕК |
|3.Пара відсутня      |  -  |
|4.Пара відсутня      |  -  |
+---------------------+-----+
|       ПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    4: """<pre>
+---------------------------+
|           ЧЕТВЕР          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Комп. сис. шт. інт.| ЛЕК |
|2.Проектування МПС   | ЛАБ |
|3.Пара відсутня      |  -  |
|4.Пара відсутня      |  -  |
+---------------------+-----+
|       ПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    5: """<pre>
+---------------------------+
|         П'ятниця          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Пара відсутня      |  -  |
|2.Пара відсутня      |  -  |
|3.Теорія проект. ЕОМ | ЛЕК |
|4.Фізичне виховання  |  -  |
+---------------------+-----+
|       ПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>"""
}


@bot.message_handler(func=lambda message: message.text == "/start")
def notification(message):
    user_name = message.from_user.username
    user_id = message.from_user.id
    bot.send_message(admin_max,
                     "Користувач " + str(user_name) + " намагається увійти до бота! \nID користувача - " + str(user_id))
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
        bot.send_message(message.chat.id, "Введіть пароль, щоб увійти до бота!", reply_markup=markup11)

        bot.register_next_step_handler(message, choice_start)


def choice_start(message):
    global mess
    mess = message.text
    if mess == config.PASSWORD:
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

        bot.send_message(message.chat.id, "З якої ти групи?", reply_markup=markup3)
        bot.register_next_step_handler(message, check_group)
    elif mess == "Я не знаю пароль":
        send_to_admin_mess(message)
    else:
        bot.send_message(message.chat.id, "Пароль не вірний!")
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

            file = open("am201.txt", "a")
            file.write(str(users_id) + "\n")
            file.close()

            bot.send_message(message.chat.id, "Зрозумів, ти з АМ-201!", reply_markup=markup)

    elif mess == "АМ-202":
        cursor.execute(f"SELECT user_id FROM users_202 WHERE user_id = {users_id}")
        data = cursor.fetchone()

        if data is None:
            cursor.execute('INSERT INTO users_202 VALUES (?, ?)', (username, users_id,))
            con.commit()

            file = open("am202.txt", "a")
            file.write(str(users_id) + "\n")
            file.close()

            bot.send_message(message.chat.id, "Зрозумів, ти з АМ-202!", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Спробуй ще раз вказати свою групу!", reply_markup=markup3)

    bot.send_message(admin_max, "Користувач " + str(username) + " приєднався до боту!")
    bot.send_message(message.chat.id, "Вітаю у головному меню " + str(username), reply_markup=markup)


@bot.pre_checkout_query_handler(lambda query: True)
def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    bot.answer_pre_checkout_query(int(pre_checkout_q.id), ok=True)


@bot.message_handler(func=lambda message: message.text == "/pay")
def pay(message):
    bot.send_invoice(message.chat.id,
                     title="Підписка на бота",
                     description="Активація підписки на місяць",
                     provider_token=config.PAYMENTS_TOKEN,
                     currency="uah",
                     photo_url="https://i.postimg.cc/jjG15PB7/user-mara-a-fat-caracal-style-money-in-hand-8k-6aac55f9-3a0f-4aa9-817b-5decdb86ee87.png",
                     photo_width=606,
                     photo_height=606,
                     photo_size=416,
                     is_flexible=False,
                     prices=[PRICE],
                     invoice_payload="PAYMENT")


@bot.message_handler(func=lambda message: message.text == "⬅НАЗАД")
def ui(message):
    sti = open('AnimatedSticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    text = ['Слава Україні, козаче!', 'А ну скажи паляниця!', 'Хто не скаче - той москаль!', 'Смерть пуйлу!',
            'Скільки танків вже вкрав?']
    fraz = random.randint(0, int(len(text)) - 1)
    bot.send_message(message.chat.id, text[fraz], reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "send" and message.chat.type == 'private')
def send_mess(message):
    bot.send_message(message.chat.id, "Отправляйте нужное сообщение!")
    bot.register_next_step_handler(message, reg_message_news)


def reg_message_news(message):
    global mess
    mess = message.text
    if mess == "close":
        bot.send_message(message.chat.id, "Скасувано!", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Повідомлення відправлено!", reply_markup=markup)
        con = sqlite3.connect("my.db")
        cursor = con.cursor()
        cursor.execute("SELECT user_id FROM users")
        records = cursor.fetchall()

        for us in records:
            try:
                bot.send_message(us[0], mess)
            except:
                pass
        con.close()


@bot.message_handler(func=lambda message: message.text == "📒Пари📒" and message.chat.type == 'private')
def par(message):
    con = sqlite3.connect("my.db")
    cursor = con.cursor()

    day = datetime.now().isoweekday()
    week = datetime.now().isocalendar().week + 1
    time_before_send = time(10, 00, 00).strftime("%H:%M:%S")
    time_now = datetime.now().strftime("%H:%M:%S")

    if time_now > time_before_send and day != 5 and day != 6 and day != 7:
        day += 1
    elif (time_now > time_before_send and day == 5) or (day == 6) or (day == 7):
        day = 1; week += 1

    user_id = message.from_user.id
    cursor.execute(f"SELECT user_id FROM users_201 WHERE user_id = {user_id}")
    data = cursor.fetchone()

    if str(user_id) in str(data):
        if week % 2 != 0:
            bot.send_message(message.chat.id, am_201_schedule_n_p.get(day), reply_markup=markup7, parse_mode='HTML')
        else:
            bot.send_message(message.chat.id, am_201_schedule_p.get(day), reply_markup=markup7, parse_mode='HTML')

    cursor.execute(f"SELECT user_id FROM users_202 WHERE user_id = {user_id}")
    data = cursor.fetchone()

    if str(user_id) in str(data):
        if week % 2 != 0:
            bot.send_message(message.chat.id, am_202_schedule_n_p.get(day), reply_markup=markup7, parse_mode='HTML')
        else:
            bot.send_message(message.chat.id, am_202_schedule_p.get(day), reply_markup=markup7, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == "‍🧑‍🎓Студенти🧑‍🎓" and message.chat.type == 'private')
def profile7(message):
    bot.send_message(message.chat.id, "Обери групу!", reply_markup=markup2)


@bot.message_handler(func=lambda message: message.text == "🕛Дзвоник🕛" and message.chat.type == 'private')
def profile9(message):
    bot.send_message(message.chat.id, """<pre>
+---------------------------+
|          ДЗВІНКИ          |
+---------------------------+
|1.      08:00 - 09:35      |
|2.      09:50 - 11:25      |
|3.      11:40 - 13:15      |
|4.      13:30 - 15:05      |
+---------------------------+
</pre>""", reply_markup=markup, parse_mode="HTML")


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    global group
    if call.data == "1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="""<pre>
+-------------------------------+
|             AM-201            |
+--+----------------------------+
|№ |            ПІБ             |        
+--+----------------------------+
|1 |Авдєєнко Олександр Олегович |
|2 |Арутюнов Артем Артурович    |
|3 |Бельчік Кирило Борисович    |
|4 |Демиденко Микита Олександр. |
|5 |Денисюк Діана Олександрівна |
|6 |Ємець Андрій Віталійович    |
|7 |Михайленко Дмитро Вячеслав. |
|8 |Михайленко Сергій Вячеслав. |
|9 |Міхов Андрій Ігорович       |
|10|Орлов Роман Георгійович     |
|11|Смаль Максим Анатолійович   |
|12|Трубчанін Максим Костянтин. |
|13|Черних Кіріл Михайлович     |
|14|Яковенко Дмитро Вікторович  |
|15|Гьоккая Семіх               |
|16|Джауак Анас                 |
|17|Хазирлар Хюсеїна            |
|18|Ребець Ілля Вадимович       |
|19|Ткачук Руслан Дмитрович     |
|20|Воронов Олег Дмитрович      |
|21|Кліпов Владислав Олекс.     |
+--+----------------------------+
</pre>""", reply_markup=markup202, parse_mode="HTML")
    elif call.data == "2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="""<pre>
+-------------------------------+
|             AM-202            |
+--+----------------------------+
|№ |            ПІБ             |        
+--+----------------------------+
|1 |Баланєл Валентин Юрійович   |
|2 |Безугла Аліна Ігорівна      |
|3 |Брашкін Костянтин Юрійович  |
|4 |Бабіч Костянтин             |
|5 |Гаврилов Микита Дмитрович   |
|6 |Димитров Олександр Марч.    |
|7 |Кочков Роман Борисович      |
|8 |Красильников Андрій Олекс.  |
|9 |Куруч Микита Володимирович  |
|10|Магденко Михайло Волод.     |
|11|Сакал Тимофій Юрійович      |
|12|Сєрооченко Микита           |
|13|Стринаглюк Іван Іванович    |
|14|Сушко Олексій Володимирович |
|15|Янчук Володимир Олекс.      |
|16|Абудхер Адель Мохамед Алі   |
|17|Пожидаєв Максим Волод.      |
|18|Ткаченко Олег Iгорович      |
|19|Ткачова Тетяна              |
|20|Ліхненко Дмитро Андрійович  |
|21|Залевський Микола Олегович  |
+--+----------------------------+
</pre>""", reply_markup=markup201, parse_mode="HTML")
    elif call.data == "3":
        group = "AM-201"
        check_group(call.message)
    elif call.data == "4":
        group = "AM-202"
        check_group(call.message)
    elif call.data == "5":
        day = datetime.now().isoweekday()
        week = datetime.now().isocalendar().week + 1
        user_id = call.message.chat.id
        con = sqlite3.connect("my.db")
        cursor = con.cursor()
        full_schedule = ""

        if day == 6 or day == 7:
            week += 1

        cursor.execute(f"SELECT user_id FROM users_201 WHERE user_id = {user_id}")
        data = cursor.fetchone()
        cursor.execute(f"SELECT user_id FROM users_202 WHERE user_id = {user_id}")
        data_2 = cursor.fetchone()

        if str(user_id) in str(data):
            if week % 2 != 0:
                for i in range(5):
                    full_schedule += am_201_schedule_n_p.get(i + 1) + "\n"
            else:
                for i in range(5):
                    full_schedule += am_201_schedule_p.get(i + 1) + "\n"
        elif str(user_id) in str(data_2):
            if week % 2 != 0:
                for i in range(5):
                    full_schedule += am_202_schedule_n_p.get(i + 1) + "\n"
            else:
                for i in range(5):
                    full_schedule += am_202_schedule_p.get(i + 1) + "\n"

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<pre>" + full_schedule + "</pre>", reply_markup=markup8, parse_mode="HTML")
    elif call.data == "6":
        con = sqlite3.connect("my.db")
        cursor = con.cursor()
        day = datetime.now().isoweekday()
        week = datetime.now().isocalendar().week + 1
        time_before_send = time(10, 00, 00).strftime("%H:%M:%S")
        time_now = datetime.now().strftime("%H:%M:%S")

        if time_now > time_before_send and day != 5 and day != 6 and day != 7:
            day += 1
        elif (time_now > time_before_send and day == 5) or (day == 6) or (day == 7):
            day = 1; week += 1

        user_id = call.message.chat.id
        cursor.execute(f"SELECT user_id FROM users_201 WHERE user_id = {user_id}")
        data = cursor.fetchone()

        if str(user_id) in str(data):
            if week % 2 != 0:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=am_201_schedule_n_p.get(day), reply_markup=markup7, parse_mode="HTML")
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=am_201_schedule_p.get(day), reply_markup=markup7, parse_mode="HTML")

        cursor.execute(f"SELECT user_id FROM users_202 WHERE user_id = {user_id}")
        data = cursor.fetchone()

        if str(user_id) in str(data):
            if week % 2 != 0:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=am_202_schedule_n_p.get(day), reply_markup=markup7, parse_mode="HTML")
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=am_202_schedule_p.get(day), reply_markup=markup7, parse_mode="HTML")


@bot.message_handler(func=lambda message: message.text == "Я не знаю пароль" and message.chat.type == 'private')
def send_to_admin_mess(message):
    bot.send_message(message.chat.id, "Напишіть ПІБ та групу!", reply_markup=markup5)
    bot.register_next_step_handler(message, reg_mess_admin)


def reg_mess_admin(message):
    global mess, id_from_user
    mess = message.text
    if mess == "Відмінити":
        send_welcome(message)
    else:
        id_from_user = message.from_user.id
        user_name = message.from_user.username
        bot.send_message(message.chat.id, "Запит відправлений! Очікуйте відповіді!")
        bot.send_message(admin_max, "Запит на пароль від: " + str(user_name) + "\n" + mess,
                         reply_markup=markup13)
        send_welcome(message)


@bot.message_handler(func=lambda message: message.text == "Відправити" and message.chat.type == 'private')
def solution_send(message):
    global id_from_user
    bot.send_message(message.chat.id, f"Користувачу з id {id_from_user} доступ відкритий!", reply_markup=markup)
    bot.send_message(id_from_user, "Пароль: QWERTY20X", reply_markup=markup11)


def starting_checking_201():
    while True:
        current_time = tm.strftime("%H:%M")
        today = tm.strftime("%A")
        schedule_201 = get_schedule_am_201(today)
        if current_time in schedule_201:
            con = sqlite3.connect("my.db")
            cursor = con.cursor()
            cursor.execute("SELECT user_id FROM users_201")
            records = cursor.fetchall()

            subject = schedule_201[current_time].split("-")
            for us in records:
                try:
                    bot.send_message(us[0], f"Пара - {subject[0]}\nПосилання - {subject[1]}",
                                     disable_web_page_preview=True, reply_markup=markup, parse_mode="HTML")
                    tm.sleep(0.2)
                except Exception:
                    print("error send")

            con.close()
            tm.sleep(60)
        tm.sleep(1)


def starting_checking_202():
    while True:
        current_time = tm.strftime("%H:%M")
        today = tm.strftime("%A")
        schedule_202 = get_schedule_am_202(today)
        if current_time in schedule_202:
            con = sqlite3.connect("my.db")
            cursor = con.cursor()
            cursor.execute("SELECT user_id FROM users_202")
            records = cursor.fetchall()

            subject = schedule_202[current_time].split("-")
            for us in records:
                try:
                    bot.send_message(us[0], f"Пара - {subject[0]}\nПосилання - {subject[1]}",
                                     disable_web_page_preview=True, reply_markup=markup, parse_mode="HTML")
                    tm.sleep(0.2)
                except Exception:
                    print("error send")

            con.close()
            tm.sleep(60)
        tm.sleep(1)


def main():
    try:
        p_1 = multiprocessing.Process(target=starting_checking_201, args=())
        p_1.start()
        p_2 = multiprocessing.Process(target=starting_checking_202, args=())
        p_2.start()
        bot.infinity_polling(none_stop=True)
    except Exception:
        pass


if __name__ == '__main__':
    main()
