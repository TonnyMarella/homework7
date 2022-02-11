import socket as skt

srv = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

srv.bind(("127.0.0.1", 8888))

srv.listen()
print("Server is listening")
srv.setblocking(False)

users = list()
msgs = {}
noCon = False

while True:
    try:
        user, address = srv.accept()
        print(f"user {user}, address {address} IS CONNECTED", users, msgs)
    except skt.error:
        if noCon is False:
            print("No connections")
            noCon = True
    else:
        user.setblocking(True)
        result = user.recv(1024)

        c_user, w_user = result.decode("utf-8").split(":")
        user.send(b"You are connected")
        if w_user in msgs.keys() and len(msgs[w_user]) > 0:
            user.send(f"You have some messages from {w_user}: ".encode("utf-8"))
        if len(users) == 0:
            users = (c_user, w_user)
        else:
            if c_user not in users:
                users.append(c_user)
            if w_user not in users:
                users.append(w_user)

        print(c_user, " connected", users)

        if len(users) > 0 and len(msgs) > 0 and c_user in msgs.keys() and len(msgs[c_user]) > 0:
            print("your msgs was not sent to receiver")
            user.send("your msgs was not sent to receiver".encode("utf-8"))
        else:
            user.send("you doesn't have any new messages".encode("utf-8"))

        if len(users) > 0 and len(msgs) > 0 and w_user in msgs.keys() and len(msgs[w_user]) > 0:
            user.send(msgs[w_user].encode("utf-8"))
            print(f"msg from {w_user} was sent, any new msgs for this user")
            msgs[w_user] = ""

        while True:
            try:
                print("result")
                result = user.recv(1024)
                print(result)
            except:
                print("no any accepted socket")
                noCon = False
                break
            else:
                noCon = False
                try:
                    name, value = result.decode("utf-8").split(":")
                    if len(value) > 1:
                        user.send(b"Your msg was delivered to server")
                        print("Message:", value)

                except ValueError:
                    user.send(f"any new msgs for {c_user}".encode("utf-8"))

                else:
                    # print(name, ": ", value)
                    if value != "exit" and value != "" and value != "1":
                        if name in msgs.keys():
                            msgs[name] += " ... NEXT: " + value
                        else:
                            msgs = {name: value}
                        print(msgs[name])
                    elif len(users) > 0 and len(msgs) < 2 and c_user in msgs.keys() and len(msgs[c_user]) > 0:
                        user.send("your msgs was not sent to receiver".encode("utf-8"))
                    # print(users)
                    if value == "exit":
                        user.close()