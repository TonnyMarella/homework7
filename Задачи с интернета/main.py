from Server import Socket
import asyncio


class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()

        self.socket.listen(5)
        print("Server is listening")

        self.users = []

    def set_up(self):
        self.socket.bind(("127.0.0.1", 9898))
        self.socket.setblocking(False)

    async def send_date(self, date):
        for users in self.users:
            users.send(date)

    async def listen_socket(self, listened_socket=None):
        print("Listening users")

        while True:
            date = listened_socket.recv(2048)
            print("User send:", date)

            self.send_date(date)

    async def accept_socket(self):
        while True:
            user_socket, address = await self.accept()
            print("User is connected", user_socket)

            self.users.append(user_socket)
            listen_accept_user =


if __name__ == "__main__":
    server = Server()
    server.set_up()

    server.start()