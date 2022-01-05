import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("", 3030))

while 1:
    message = input("Что ты ответишь серверу")

    client.send(message.encode("utf-8"))

    if message == 'q':
        break

    reply = client.recv().decode("utf-8")

    print("Сервер ответил", reply)

client.close()