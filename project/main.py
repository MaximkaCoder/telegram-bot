# -*- coding: utf-8 -*-
# !/usr/bin/python3.9
import random
from datetime import datetime
from datetime import time
import sqlite3
import config
import telebot
from telebot import types
import multiprocessing
import time as tm
import os

token_number = int(os.environ.get('TOK_NUM'))
bot = telebot.TeleBot(config.TOKEN[token_number])

admin_max = config.ADMIN_MAX
admin_alina = config.ADMIN_ALINA
admin_vova = config.ADMIN_VOVA

PRICE = types.LabeledPrice(label="Підписка на 1 місяць", amount=10*100)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("📚Пари📚")
item2 = types.KeyboardButton("‍🧑‍🎓Студенти🧑‍🎓")
item3 = types.KeyboardButton("⌛Дзвоник⌛")

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
item = types.KeyboardButton("Відправити")
item2 = types.KeyboardButton("⬅НАЗАД")
markup13.add(item, item2)

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
    5:"""<pre>
+---------------------------+
|         П'ятниця          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Теорія проект. ЕОМ | ЛЕК |
|2.Пара відсутня      |  -  |
|3.Пара відсутня      |  -  |
|4.Фізичне виховання  |  -  |
+---------------------+-----+
|     НЕПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
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
|3.Сис. реальн. часу  | ЛЕК |
|4.Пара відсутня      |  -  |
+---------------------+-----+
|       ПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
    5:"""<pre>
+---------------------------+
|         П'ятниця          |
+---------------------+-----+
|          ПАРИ       | ТИП |
+---------------------+-----+
|1.Теорія проект. ЕОМ | ЛЕК |
|2.Пара відсутня      |  -  |
|3.Пара відсутня      |  -  |
|4.Фізичне виховання  |  -  |
+---------------------+-----+
|       ПАРНИЙ ТИЖДЕНЬ      |
+---------------------------+
</pre>""",
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


@bot.message_handler(func=lambda message: message.text == "📚Пари📚" and message.chat.type == 'private')
def par(message):
    con = sqlite3.connect("my.db")
    cursor = con.cursor()

    day = datetime.now().isoweekday()
    week = datetime.now().isocalendar().week + 1
    time_before_send = time(9, 00, 00).strftime("%H:%M:%S")
    time_now = datetime.now().strftime("%H:%M:%S")

    if time_now > time_before_send and day != 5:
        day += 1
    elif (time_now > time_before_send) and (day == 5 or day == 6 or day == 7):
        day = 1; week += 1

    user_id = message.from_user.id
    cursor.execute(f"SELECT user_id FROM users_201 WHERE user_id = {user_id}")
    data = cursor.fetchone()

    if str(user_id) in str(data):
        am_201_schedule_n_p.get(day)
        if week % 2 != 0:
            bot.send_message(message.chat.id, am_201_schedule_n_p.get(day), reply_markup=markup, parse_mode='HTML')
        else:
            bot.send_message(message.chat.id, am_201_schedule_p.get(day), reply_markup=markup, parse_mode='HTML')

    cursor.execute(f"SELECT user_id FROM users_202 WHERE user_id = {user_id}")
    data = cursor.fetchone()

    if str(user_id) in str(data):
        bot.send_message(message.chat.id, "Тут буде розклад для групи АМ-202", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "‍🧑‍🎓Студенти🧑‍🎓" and message.chat.type == 'private')
def profile7(message):
    bot.send_message(message.chat.id, "Обери групу!", reply_markup=markup2)


@bot.message_handler(func=lambda message: message.text == "⌛Дзвоник⌛" and message.chat.type == 'private')
def profile9(message):
    bot.send_message(message.chat.id, """<pre>
+-----------------------------+
|           ДЗВІНКИ           |
+--------------+--------------+
| 1-а полупара | 2-а полупара |        
+--------------+-------+------+
|1. 8:00-8:45  |   8:50-9:35  |
|2. 9:50-10:35 |  10:40-11:25 |
|3.11:40-12:25 |  12:30-13:15 |        
|4.13:30-14:15 |  14:20-15:05 |             
+--------------+--------------+
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
        id_from_user =message.from_user.id
        user_name = message.from_user.username
        bot.send_message(message.chat.id, "Запит відправлений! Очікуйте відповіді!")
        bot.send_message(admin_max, "Запит на пароль від: " + str(user_name) + "\n" + mess,
                         reply_markup=markup13)
        send_welcome(message)


@bot.message_handler(func=lambda message: message.text == "Відправити" and message.chat.type == 'private')
def solution_send(message):
    global id_from_user
    bot.send_message(message.chat.id, f"Користувачу з id {id_from_user} доступ відкритий!", reply_markup=markup)
    bot.send_message(id_from_user, "Доступ відкритий! \nПароль: QWERTY20X", reply_markup=markup11)


def get_schedule_am_201(day):
    if day == "Monday":
        return {
            "07:45": "Міжмашинна взаємодія-???",
            "09:35": "Системи реального часу-https://cutt.ly/d8EvFz9",
            "11:25": "Системи реального часу-https://cutt.ly/d8EvFz9"
        }
    elif day == "Tuesday":
        return {
            "07:45": "Вибіркова дисципліна-???",
            "09:35": "Системи реального часу-https://cutt.ly/d8EvFz9",
            "11:25": "Міжмашинна взаємодія-???"
        }
    elif day == "Wednesday":
        return {
            "05:55": "Вибіркова дисципліна-???",
            "07:45": "Проектування МПС-???"
        }
    elif day == "Thursday":
        return {
            "05:55": "Комп'ютерні системи штучного інтелекту-https://cutt.ly/x8Ev3Lh",
            "07:45": "Проектування МПС-???",
            "09:35": "Системи реального часу-https://cutt.ly/d8EvFz9"
        }
    elif day == "Friday":
        return {
            "09:35": "Теорія проектування ЕОМ-https://cutt.ly/E8EbpjF",
            "11:25": "Фізичне виховання-???"
        }
    elif day == "Saturday":
        return {
            "08:00": "Видумана дисципліна-https://cutt.ly/w8c7YiN",
            "09:50": "Видумана дисципліна-???",
            "11:40": "Видумана дисципліна-???"
        }


def starting_checking():
    while True:
        current_time = tm.strftime("%H:%M")
        today = tm.strftime("%A")
        schedule_201 = get_schedule_am_201(today)
        if current_time in schedule_201:
            subject = schedule_201[current_time].split("-")
            bot.send_message(admin_max, f"Через 5 хвилин почнеться пара '{subject[0]}'!\nПосилання на пару: {subject[1]}", reply_markup=markup)
            tm.sleep(60)
        tm.sleep(1)


def main():
    try:
        p = multiprocessing.Process(target=starting_checking, args=())
        p.start()
        bot.infinity_polling(none_stop=True)
    except Exception:
        pass


if __name__ == '__main__':
    main()