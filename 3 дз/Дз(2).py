
import sys

x = int(input("Введите значение x от -10 до 10\n"))

if x > 10 or x < -10:
    print("Вы ввели неправильное значение")
    sys.exit()
else:
    pass
if x > -5 and x < 5:
    y = x ** 2
    print("Ваш результат: y =", y)
elif x < -5:
    y = 2 * abs(x) - 1
    print("Ваш результат: y =", y)
else:
    y = 2 * x
    print("Ваш результат: y =", y)