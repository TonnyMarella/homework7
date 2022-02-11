# Задание 1 Создать простой чат, на основе TCP протокола
# , который позволит подключаться нескольким клиентам
# и обмениваться сообщениями.
# CLIENT
import socket as skt

client_name = "First"

msg = input("Введите имя получателя (second): ")

client = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

client.connect(("127.0.0.1", 8888))

client.send((client_name + ":" + msg.title()).encode("utf-8"))

while True:
    data = client.recv(1024)
    print(data.decode("utf-8"))
    msg = input("введите сообщение (exit-выход): ")
    if len(msg) > 0:
        client.send((client_name + ":" + msg).encode("utf-8"))
    if msg == "exit":
        break