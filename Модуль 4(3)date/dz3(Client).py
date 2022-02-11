import socket
import asyncio


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 7070))
print("Вы подключились к серверу")


def listen():
    print(client.recv(1024).decode('utf-8'))
    send()


def send():
    while True:
        client.send(input(":::").encode('utf-8'))
        date = client.recv(1024).decode('utf-8')
        print('Результат:', date)


listen()

# async def main():
#     loop.create_task(listen())
#     loop.create_task(send())
#
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.run_forever()
