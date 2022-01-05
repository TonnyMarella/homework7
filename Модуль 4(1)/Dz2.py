# Функция декоратор которая оставляет в коненом итоге только нечётные числа
def decor(func):
    def inner(*args):
        lst = [i for i in list(func(*args)) if i % 2 != 0]
        return lst
    return inner


# Функция по нахождению "n" чисел Фибоначчи
@decor
def fibo(n):
    fib1, fib2 = 0, 1
    for i in range(2, n + 1):
        yield fib2
        fib1, fib2 = fib2, fib1 + fib2


print(fibo(20))
