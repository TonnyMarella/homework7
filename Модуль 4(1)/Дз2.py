# Cделать простой сервер, который принимает клиента и пишет информацию о нём

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 7070))

server.listen(2)
print('Начать чат! ')


conn, addr = server.accept()


while 1:

    print("К серверу подключился:", conn, "\nс адресом:", addr)
    message = conn.recv(1024).decode("utf-8")
    if message == 'q':
        break


server.close()

conn.close()
