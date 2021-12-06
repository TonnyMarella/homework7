def first(x):
    return x * 2


def second(x):
    return x ** 2


def main():
    i = -5
    while i < 5:
        i += 0.5
        print("Первая функция ", i, " = ", first(i), "\t",  end='', sep='')
        print("Вторая функция ", i, " = ", second(i), sep='')


main()
