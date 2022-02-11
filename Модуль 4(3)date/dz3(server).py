# Разработайте сокет сервер на основе библиотеки asyncio.
# Сокет сервер должен выполнять сложение двух чисел, как из предыдущего примера по многопоточност

import socket
import asyncio

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 7070))
server.listen(4)

users = []

print('Начать чат! ')


async def listening_users(user):
    print("Listening users")
    user.send("Введите два числа которые вы хотите сложить через пробел.\n"
              "Например(2 2)(Возможно только сложение)".encode('utf-8'))
    while True:
        date = await loop.sock_recv(user, 1024)
        print("User sent", date)
        numbers = date.decode('utf-8').split()
        result = str(int(numbers[0]) + int(numbers[1]))
        user.send(result.encode('utf-8'))
        await asyncio.sleep(0.1)


async def start_server():
    while True:
        conn, addr = await loop.sock_accept(server)
        print("Подключился user:", addr[0])
        users.append(conn)
        await listening_users(conn)


async def main():
    loop.create_task(start_server())
    loop.create_task(start_server())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()