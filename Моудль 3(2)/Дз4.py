class Car:
    def __init__(self, mark, color, motor):
        self.mark = mark
        self.color = color
        self.motor = motor

    def info(self):
        print(f'Машина марки {self.mark}, цвета {self.color}, с мотором {self.motor}')


class Reno(Car):
    def logan(self):
        print("Бюджетная машина")
        Car.info(self)


class Toyota(Car):
    def prado(self):
        print("Статусная машина")
        Car.info(self)


class Lexus(Toyota):
    def rx370(self):
        Toyota.prado(self)


c1 = Reno("Logan", "White", "1,6")
c1.logan()
c2 = Toyota("Toyota Prado", "Black", "3,5")
c2.prado()
c3 = Lexus("RX370", "Black", "3,0")
c3.rx370()
