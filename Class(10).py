class Robot:
    POPULATION = 0

    def __init__(self, name):
        self.name = name
        print("Робот {} был создан".format(self.name))
        Robot.POPULATION += 1

    def destroy(self):
        Robot.POPULATION -= 1
        print("Робот {}, был уничтожен".format(self.name))
        self.name = None

    def say_hello(self):
        print("Робот {} приветствует тебя, особь человеческого рода".format(self.name))

    @classmethod
    def how_many(cls):
        print("{}, вот сколько нас еще осталось".format(cls.POPULATION))


r2 = Robot("R2-D2")
r2.say_hello()
Robot.how_many()
r2.destroy()
Robot(name="R1-D1")
Robot(name="R3-D3")
r2.destroy()
print(Robot.POPULATION)
print(r2.POPULATION)
