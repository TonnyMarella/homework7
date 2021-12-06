class English:
    @staticmethod
    def greeting():
        print("Hello my friend")


class Spanish:
    @staticmethod
    def greeting():
        print("Hola mi amigo")


f1 = English
f2 = Spanish


def hello_friend():
    f1.greeting()
    f2.greeting()


hello_friend()

