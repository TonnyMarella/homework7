import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5050))

server.listen(2)

conn, addr = server.accept()

