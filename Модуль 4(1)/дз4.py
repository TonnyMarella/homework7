# Создайте обычную функцию умножения двух чисел. Частично примените её к одному аргументу.
# Создайте каррированную функцию умножения двух чисел. Частично примените её к одному аргументу.
from functools import partial

def mul(x, y):
    return x * y

result = partial(mul, 10)

print(result(3))


# Каррирование

def ymn(x):
    def result(y):
        return x * y
    return result

print(ymn(2)(2))