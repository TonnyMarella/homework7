class Car:
    AUTO = []
    AUTO_PRICE = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Car.AUTO.append(self.name)
        Car.AUTO_PRICE.append(self.price)

    @staticmethod
    def all_car(self):
        return Car.AUTO


class ShowRoom:
    @staticmethod
    def sell(self, mark):
        del Car.AUTO[mark]
        del Car.AUTO_PRICE[mark]

    # Функция sell удаляет из списка машин, машину которую пользователь согласился купить
    # Класс hello привествует человека в "АвтоСалоне" предлагает на выбор список машин которые сейчас есть,
    # И если человек остановил свой выбор на какой либо машине, пользователю сообщают сумму и уточняют желает
    # ли он купить данный автомобиль, если да, машина и цена удаляется из списка

    @staticmethod
    def hello(self):
        mark = input(f"Приветствую ваш в нашем салоне, вот список наших машин {Car.AUTO}\n"
                     f"Какая марка вас интересует?\n")
        if Car.AUTO.count(mark) > 0:
            mark = Car.AUTO.index(mark)
            choice = input(f'Марка {Car.AUTO[mark]}, цена {Car.AUTO_PRICE[mark]}\n'
                           f'Будете покупать?(y/n)\n')
            if choice == 'y':
                ShowRoom.sell(Car.AUTO[mark], mark)
        else:
            print('К сожалению данной марки у нас сейчас нету')


a1 = Car("BMW", 10000)
a1 = Car("Ford", 4000)
a1 = Car("Reno", 3000)

ShowRoom.hello(a1)

print(Car.all_car(a1))

a1 = Car("Mazda", 6000)
print(Car.all_car(a1))
