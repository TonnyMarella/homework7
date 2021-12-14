# Возможно я не доконца понял смысл задачи, поэтому если вдруг в этой или последующих трёх задач
# Будет что то неправильно, я переделаю :)

class Car:
    def __init__(self, mark, color, motor):
        self.mark = mark
        self.color = color
        self.__motor = motor

    # Инкапсулировали мотор, теперь доступ к нему на прямую происходить не может, мы можем менять значения
    # мотора только через метод auto, реализовали это с помощью декоратора Property, где property служит
    # get'oм, а ниже auto.setter - setter'ом

    @property
    def auto(self):
        return f'{self.mark}, {self.color}, {self.__motor}'

    @auto.setter
    def auto(self, motor):
        self.__motor = motor


a1 = Car("BMW", "White", 2.0)

# Видим что к цвету и марке можем обратиться сразу, но к мотору только через геттер, тоесть метод auto

print(a1.auto)
print(a1.color)
print(a1.mark)
a1.auto = 3.0
print(a1.auto)
