class NegativeValueException(Exception):
    pass


def plus(a, b):
    print(a + b)


def minus(a, b):
    print(a / b)


def mult(a, b):
    print(a / b)


def div(a, b):
    print(a / b)


def stepen(a, b):
    try:
        print(a ** b)
    except ZeroDivisionError:
        print("Операция возведения 0 в отрицательную степень невозможна")


while True:

    do = input("Введите действие которое вы хотите совершить\n")
    a = int(input("Введите первое число\n"))
    b = int(input("Введите второе число\n"))

    if do == '+':
        plus(a, b)
    elif do == "-":
        minus(a, b)
    elif do == "*":
        mult(a, b)
    elif do == "/":
        try:
            div(a, b)
            break
        except ZeroDivisionError:
            print("Деление на 0 невозможно")
    elif do == "**":
            stepen(a, b)
    else:
        print("Введите корректную операцию")

    x = input("Желаете повторить? (y/n) ").lower()
    if x != 'y':
        break
