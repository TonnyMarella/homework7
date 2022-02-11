# Для таблицы «материала» из дополнительного задания создайте пользовательскую агрегатную функцию,
# которая считает среднее значение весов всех материалов результирующей выборки и округляет данной значение до целого

import sqlite3


try:
    sqlite_connection = sqlite3.connect("homework.db")
    cursor = sqlite_connection.cursor()
    print("SLite3 подключен")
    sqlite_create_table_query = """CREATE TABLE IF NOT EXISTS material(
        id INTEGER PRIMARY KEY,
        weight TEXT NOT NULL,
        height INTEGER NOT NULL
        )"""
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    while True:
        choice = input("1.Добавить материал.\n2.Показать все материалы."
                       "\n3.Посчитать среднее значение всех весов."
                       "\n4.Выйти\n")
        if choice == "1":
            weig = int(input("Введите вес материала:\n"))
            heig = int(input("Введите высоту материала:\n"))
            cursor.execute("INSERT INTO material (weight, height) VALUES(?, ?)", (weig, heig,))
            sqlite_connection.commit()
        if choice == "2":
            date = cursor.execute("SELECT * FROM material").fetchall()
            print(date)
        if choice == "3":
            all_weight = cursor.execute('SELECT weight FROM material').fetchall()
            result = 0
            for i in all_weight:
                result += int(i[0])
            print("Средний вес материалов:", int(result/len(all_weight)))
        elif choice == "4":
            break
        else:
            print("Введите корректную операцию")

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)