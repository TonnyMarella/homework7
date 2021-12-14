# Возможно я не совсем правильно понял суть задачи, но сделал как понял:)
class MyError(Exception):
    def __init__(self, text):
        self.text = text


def error():
    raise MyError("Неправильное значение")


x = int(input("Введите значение от 0 до 10\n"))

if not 0 < x < 10:
    error()
else:
    print("Вы ввели: ", x)