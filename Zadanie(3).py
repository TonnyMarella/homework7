import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 7070))

server.listen(2)
print("Server start!")

conn, adress = server.accept()
while 1:

    client_msg = conn.recv(1024)

    if client_msg == "q":
        break

    print("Клиент пишет:", client_msg)

    lst_str = list(client_msg.decode("utf-8").split(","))
    lst_int = [int(i) for i in lst_str]
    result = str(sum(lst_int))

    print("Наш ответ:", result)
    conn.send(result.encode('utf-8'))

server.close()

conn.close()