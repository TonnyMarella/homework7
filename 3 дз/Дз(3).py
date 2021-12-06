print("ax^2 + bx + c = 0:")
a = float(input("Введите число a\n"))
b = float(input("Введите число b\n"))
c = float(input("Введите число c\n"))

D = b ** 2 - 4 * a * c
print("D = ", D)

if D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print("x1 =", x1, "x2 =", x2)
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("Корней нет")
