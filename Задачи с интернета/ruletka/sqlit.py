# Создать базу данных с игроками в казино, когда запускаешь программу у пользователя должен быть выбор
# Зарегестрироваться, посмотреть всех игроков или играть в казино. Игра в казино будет такой какой вы хотите
# у меня пользователь загадывает число от 1 до 3 и рандомом выпадает какое либо число, вся информация записывается в БД

import time
import sqlite3
from random import randint
from register import reg


def menu():
    while True:
        choice = input("Введите что вы хотите сделать:\n1.Зарегестрировать юзера.\n2.Просмотреть всех юзеров.\n"
                       "3.Играть в казино.\n4.Выйти\n")
        if choice == "1":
            reg()
        elif choice == "2":
            for i in cur.execute("SELECT * FROM users"):
                print(i)
        elif choice == "3":
            casino()
        elif choice == "4":
            break
        time.sleep(1)


def casino():
    user_login = input("Для игры в казино введите ваш логин: ")
    user_password = input("Введите ваш пароль: ")

    cur.execute("SELECT login FROM users WHERE login = (?) AND password = (?)", (user_login, user_password,))
    if cur.fetchone() is None:
        print("Такого пользователя не существует!")
        menu()

    user_cash = cur.execute("SELECT cash FROM users WHERE login = (?)", (user_login,)).fetchone()[0]
    print("Вы успешно вошли на свой аккаунт!\nНа данный момент ваш баланс:", user_cash,
          "случае победы вы удавиваете вашу сумму, в случае проигрыша -1000")

    while True:
        choice = int(input("Выберете чисто от 1 до 3\n"))
        result = randint(1, 3)
        if choice == result:
            user_cash *= 2
            print("Поздравляю вы победили!\n Ваши баланс:", user_cash)
        else:
            user_cash -= 1000
            print("Числo: ", result, "\nК сожалению вы проиграли!:(\n Ваш баланс", user_cash)
        if input("Будете ещё играть?(1 - да; 2 - нет)\n") == "2":
            cur.execute("UPDATE users SET cash = (?) WHERE login = (?)", (user_cash, user_login))
            base.commit()
            menu()
            break


base = sqlite3.connect("experement.db")
cur = base.cursor()
base.execute("""CREATE TABLE IF NOT EXISTS users(
             login TEXT,
             password TEXT,
             cash BIGINT
             )""")
base.commit()

menu()
