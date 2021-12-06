import math

print("Здраствуйте, вас приветствует приложение 'Калькулятор'")

Operation = input("""Какое действие вы хотите совершить?
Например:
- +
- -
- *
- /
- **
- sin
- cos
- tg\n""")

if Operation == "sin":
    x = int(input("Введите число\n"))
    print("Ваш результат:", math.sin(x))
elif Operation == "cos":
    x = int(input("Введите число\n"))
    print("Ваш результат:", math.cos(x))
elif Operation == "tg":
    x = int(input("Введите число\n"))
    print("Ваш результат:", math.tan(x))
elif Operation == "**":
    x = int(input("Введите число\n"))
    y = int(input("В какую степень хотите вознести?\n"))
    print("Ваш результат:", x ** y)
elif Operation == "+":
    number1 = int(input("Введите первое число\n"))
    number2 = int(input("Введите второе число\n"))
    print("Ваш результат:", number1 + number2 )
elif Operation == "-":
    number1 = int(input("Введите первое число\n"))
    number2 = int(input("Введите второе число\n"))
    print("Ваш результат:", number1 - number2 )
elif Operation == "*":
    number1 = int(input("Введите первое число\n"))
    number2 = int(input("Введите второе число\n"))
    print("Ваш результат:", number1 * number2 )
elif Operation == "/":
    number1 = int(input("Введите первое число\n"))
    number2 = int(input("Введите второе число\n"))
    print("Ваш результат:", number1 / number2 )
else:
    print("Вы ввели некорректную операцию")