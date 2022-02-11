import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(
    ('127.0.0.1', 6666)
)

server.listen()

client, adress = server.accept()

print("К нам подключился", adress[0])

client.send('Приветствую!'.encode('utf-8'))
while 1:
    client_msg = client.recv(1024)

    message = client_msg.decode('utf-8')

    if message == 'q':
        break

    print("Клиент пишет:", message)

    reply = input("Что сервер ответит:")

    client.send(reply.encode('utf-8'))

server.close()
client.close()