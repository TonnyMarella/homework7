import sqlite3

base = sqlite3.connect("experement.db")
cur = base.cursor()


def reg():
    user_login = input("Введите логин: ")
    user_password = input("Введите ваш пароль: ")
    user_cash = input("Введите ваши деньги: ")

    cur.execute(f"SELECT login FROM users WHERE login == (?)", (user_login,))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, user_cash))
        base.commit()
        print("Юзер успешно добавлен!")
    else:
        print("Данный логин уже зарегестрирован!")
