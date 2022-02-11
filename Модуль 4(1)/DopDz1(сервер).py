# Создать сервер и два клиента и чтоб клиенты смогли обмениваться сообщениями

import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 7070))
server.listen(4)

users = []

print('Начать чат! ')


def send_all(date):
    for user in users:
        user.send(date)


def listening_users(user):
    print("Listening users")
    while True:
        date = user.recv(1024)
        print("User sent", date)

        send_all(date)


def start_server():
    while True:
        conn, addr = server.accept()
        print("Подключился user:", addr[0])

        users.append(conn)
        listen_accept_user = threading.Thread(
            target=listening_users,
            args=(conn,)
        )

        listen_accept_user.start()


if __name__ == "__main__":
    start_server()
