import socket
from threading import Thread


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 7070))
print("Вы подключились к серверу")


def listen():
    while True:
        date = client.recv(1024)
        print(date.decode('utf-8'))


def send():
    listen_thread = Thread(target=listen)
    listen_thread.start()

    while True:
        client.send(input(":::").encode('utf-8'))


if __name__ == "__main__":
    send()

