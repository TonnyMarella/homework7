# Создайте функцию по вычислению факториала числа. Запустите несколько задач,
# используя ThreadPoolExecutor и замерьте скорость их выполнения

import concurrent.futures as pool
import time


def factorial():
    n = 20
    fac = 1

    for i in range(2, n+1):
        fac *= i
        fac = fac ** 2


def factorial1():
    n = 20
    fac = 1
    for i in range(2, n+1):
        fac *= i
        fac = fac ** 2


executor = pool.ThreadPoolExecutor(max_workers=3)
start = time.time()
A = executor.submit(factorial)
B = executor.submit(factorial1)
print("Время1:", time.time() - start)