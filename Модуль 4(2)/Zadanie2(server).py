import socket

hello = "Здраствуй Юзер, введи свой логин"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 6060))

server.listen()

user, port = server.accept()

while 1:
    login = user.recv(1024)
    # Полученная информация закодирована и должна быть расшифрована здесь
    client_msg = login.decode('utf-8')
    print("Сообщение от", client_msg, "\n")

