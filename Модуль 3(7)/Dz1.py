from statistics import mean


def average(first, second):
    list1 = []
    print("Среднее арифметическое двух чисел:", (first + second) / 2)
    for i in range(first, second + 1):
        list1.append(i)
    print(list1)
    print("Среднее арифметическое промежутка:", mean(list1))


average(10, 20)