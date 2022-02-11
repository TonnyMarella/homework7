# Cделать простой клиент, который подключается к серверу

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 7070))

while True:
    exit = input("Задача для первого задания выполнена, введите (q) для выхода)")

    client.send(exit.encode('utf-8'))
    if exit == "q":
        break
    else:
        print("Вы не можете ничего делать здесь")
