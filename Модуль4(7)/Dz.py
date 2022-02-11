# Используя модуль sqlite3 и модуль smtplib, реализуйте реальное добавление пользователей в базу.
# Должны быть реализовать следующие функции и классы: - класс пользователя, содержащий в себе следующие методы:
# get_full_name (ФИО с разделением через пробел: «Петров Игорь Сергеевич»),
# get_short_name (ФИО формата: «Петров И. С.»), get_age (возвращает возраст пользователя,
# используя поле birthday типа datetime.date); метод __str__ (возвращает ФИО и дату рождения).
# - функция регистрации нового пользователя (принимаем экземпляр нового пользователя и отправляем Email на
# почту пользователя с благодарственным письмом). - функция отправки Email с благодарственным письмом.
# - функция поиска пользователей в таблице users по имени, фамилии и почте.
# P.S. Функцию по отправке письма на email закоментил чтоб не палить свой аккаунт, если захотите проверить
# вместо login и password введите свой логин почты и пароль

import sqlite3 as sq
import smtplib
from datetime import date


base = sq.connect('Users.db')
cur = base.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                full_name TEXT NOT NULL,
                short_name TEXT NOT NULL,
                birthday TEXT NOT NULL,
                email TEXT NOT NULL,
                UNIQUE(full_name, short_name, email))
                ''')


class User:
    def __init__(self, get_full_name, get_short_name, get_age, email):
        self.get_full_name = get_full_name
        self.get_short_name = get_short_name
        self.get_age = get_age
        self.email = email
        now = date.today()
        years = []
        for i in get_age.split():
            years.append(int(i))
        birthday = date(years[0], years[1], years[2])
        self.get_age = int((now - birthday).days / 365)

    def date_base(self):
        cur.execute('SELECT full_name FROM users WHERE full_name = (?)', (self.get_full_name,))
        if cur.fetchone() is None:
            print("Записть в базу данных!")
            cur.execute('INSERT OR IGNORE INTO users VALUES(NULL, ?, ?, ?, ?)', (self.get_full_name, self.get_short_name,
                                                                              self.get_age, self.email))
            base.commit()
        else:
            print("Вы уже зарегестрированы!")

    def __str__(self):
        return f'ФИО: {self.get_full_name}, возраст: {self.get_age}'


def registration_users(full_name, short_name, age, email):
    user = User(full_name, short_name, age, email)
    user.date_base()
    print(user)

    # P.S. Функцию по отправке письма на email закоментил чтоб не палить свой аккаунт, если захотите проверить
    # вместо login и password введите свой логин почты и пароль

    # message = "Вы успешно зарегистрировались у нас на сайте! Поздравляем!)"
    # print(send_email(message=message))


def search_email(email):
    user = cur.execute('SELECT full_name, birthday, email FROM users WHERE email = (?)', (email,)).fetchone()
    print("Результаты по вашему запросу: ", user)


def search_name(name):
    user = cur.execute('SELECT full_name, birthday, email FROM users WHERE full_name = (?)', (name,)).fetchone()
    print("Результаты по вашему запросу: ", user)


# def send_email(message):
#     sender = 'your email'
#     passwor = 'your password'
#
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#
#     try:
#         server.login(sender, passwor)
#         server.sendmail(sender, sender, message)
#
#         return 'Сообщение отправленно удачно!'
#     except Exception as _ex:
#         return f'{_ex}\nПроверьте ваш логин или пароль!'


registration_users("Зубков Артём Дмитриевич", "Зубков А.Д.", "2000 6 14", 'temazubkov02@gmail.com')
registration_users("Кучеренко Дмитрий Александрович", "Кучеренко Д.А.", "2000 3 19", 'kucherenkodmitry12@gmail.com')
search_email("temazubkov02@gmail.com")
search_name("Кучеренко Дмитрий Александрович")