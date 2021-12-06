class Car:
    def __init__(self, mark, color, motor):
        self.mark = mark
        self.color = color
        self.motor = motor

# Создаём метод который описывает КАЖДУЮ машину
    def info(self):
        print(f'Машина марки {self.mark}, цвета {self.color}, с мотором {self.motor}')

# Создаём класс "Reno" который описывает автомобиль марки "Reno" после чего выводим особенность машины и
# обращаемся к классу родителю для вывода общей информации об авто


class Reno(Car):
    def logan(self):
        print("Бюджетная машина")
        Car.info(self)

# Создаём класс "Toyota" который описывает автомобиль марки "Toyota" после чего выводим особенность машины и
# обращаемся к классу родителю для вывода общей информации об авто


class Toyota(Car):
    def prado(self):
        print("Статусная машина")
        Car.info(self)

# Создаём класс "Lexus" который описывает автомобиль марки "Lexus", классом родителем для этого класса
# будет класс "Toyota", поскольку автомобили разные но особенности у них совпадают, после чего обращаемся
# к классу Toyota, где выводиться особенности, а класс Toyota уже обращается к классу родителя и выводит
# общую информацию по поводу автомобиль Lexus


class Lexus(Toyota):
    def rx370(self):
        Toyota.prado(self)


c1 = Reno("Logan", "White", "1,6")
c1.logan()
c2 = Toyota("Toyota Prado", "Black", "3,5")
c2.prado()
c3 = Lexus("RX370", "Black", "3,0")
c3.rx370()
