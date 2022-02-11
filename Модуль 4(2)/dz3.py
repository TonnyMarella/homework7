# Поработайте с созданием собственных диалектов, произвольно выбирая правила для CSV файлов.
# Зарегистрируйте созданные диалекты и поработайте, используя их, с созданием/чтением файлом.

import csv

csv.register_dialect('my_dialect', delimiter=':', lineterminator="\r")

with open("three.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, 'my_dialect')
    file_writer.writerow(["Имя", "Класс", "Возраст"])
    file_writer.writerow(["Женя", "3", "10"])
    file_writer.writerow(["Саша", "5", "12"])
    file_writer.writerow(["Маша", "11", "18"])

with open('three.csv', 'r', encoding='utf-8') as file:
    date = csv.reader(file)
    for row in date:
        print(row)