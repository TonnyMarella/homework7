import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(
    ("127.0.0.1", 9898)
)

while True:
    back_msg = client.recv(1024).decode('utf-8')
    print("Тебе ответили", back_msg)
    send_msg = input("Ты сказал:")
    client.send(send_msg.encode('utf-8'))
    if send_msg == 'q':
        break
client.close()