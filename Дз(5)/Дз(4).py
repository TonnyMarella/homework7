def averege(a,b,c):
    avg = ( a + b + c ) / 3
    print("Ваш результат: ", avg)

running = True

while running:
    a = int(input("Введите число a\n"))
    b = int(input("Введите число b\n"))
    c = int(input("Введите число c\n"))

    averege(a,b,c)

    running = input("Если вы хотите продолжить, введите (y/N)\n")
    if running != "y":
        running = False