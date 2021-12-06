# class Base:
#     @staticmethod
#     def method():
#         print("Hello from Base")
#
#
# class Child(Base):
#     @staticmethod
#     def method():
#         print("Hello from Child")
class Base:
    def __init__(self, name):
        self.name = name

    def method(self):
        print(f"Hello from {self.name}")


class Child(Base):
    def method(self):
        print(f"Hello from {self.name}")


a1 = Base("Base")
a2 = Child("Child")

a1.method()
a2.method()
