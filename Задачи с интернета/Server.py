import socket
import asyncio

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(
    ("127.0.0.1", 9898)
)

server.listen()
print("Server is started")
all_users = []

async def get_msg():
    pass

async send_msg():
    pass

async accept_client():
    cln_adress, _ = await server.accept()

if  __name__ = "__main__":

while True:
    cln_adress, _ = server.accept()

    if cln_adress is not all_users:
        all_users.append(cln_adress)

    cln_adress.send("Введите свое имя".encode('utf-8'))

    cln_name = cln_adress.recv(1024).decode('utf-8')

    print("К нам подключился:", cln_name)

    cln_adress.send("Вы успешно вошли в чат, теперь можете общаться".encode('utf-8'))
    massege = cln_adress.recv(1024).decode('utf-8')
    print('Пишет', cln_name + ":", massege)


main_loop = asyncio.get_event_loop()
main_loop.run_until_complete(main())
main_loop.run_forever()