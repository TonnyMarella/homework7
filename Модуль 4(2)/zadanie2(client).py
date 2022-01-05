import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.connect(("127.0.0.1", 6060))

while True:
    message = input("Вводи")
    client.send(message.encode("utf-8"))