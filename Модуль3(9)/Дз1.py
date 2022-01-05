from random import randint

with open("test1.txt", 'w', encoding='utf-8') as f:
    # С помощью генератора создаём 100000, рандомных чисел, с помощью генератора для того чтоб
    # у нас переменная "lst" не занимало потом память
    lst = (randint(1, 10000) for i in range(10001))
    for i in range(10000):
        f.write(str(next(lst)))
        f.write(" ")

with open("test1.txt", 'r', encoding='utf-8') as f:
    # Так же используем генератор и в итоге получаем то что в файле хранятся все числа, но при этом
    # ни одна переменная не хранит в себе все эти числа, что значительно экономит нашу память, и возоможно
    # быстрее работает :)
    x = (f.readline().split() for i in range(1))
    print(sum(map(int, next(x))))
