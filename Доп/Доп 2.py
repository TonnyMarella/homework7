def memory(x):
    print("Количество файлов которое у вас поместится(При файле", x, " мб): ", 1000000 / x, sep='')
    print("При этом у вас остаётся:", 1000000 % x, " мб свободно", sep="")


file = int(input("Сколько весит ваш файл\n"))

memory(file)
