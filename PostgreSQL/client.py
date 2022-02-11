import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(
    ("127.0.0.1", 6666)
)

date = client.recv(1024)

print("Сервер пишет:", date.decode('utf-8'))

def send_date(date):
    client.send(date)

def invite():
    date = client.recv(1024)
    print("Сервер пишет:", date.decode('utf-8'))
while 1:
    massage = input("Что вы ответите серверу: ")
    date = massage.encode('utf-8')
    client.send(date)

    if date == 'q':
        break

client.close()
