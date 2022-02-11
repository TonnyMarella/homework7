import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 7070))

server.listen(2)
print('Начать чат! ')


conn, addr = server.accept()

while 1:

    client_msg = conn.recv(1024)

    message = client_msg.decode('utf-8')

    if message == 'q':
        break

    print('client msg:', message)

    reply = input('Ответить:')

    conn.send(reply.encode('utf-8'))

server.close()

conn.close()
