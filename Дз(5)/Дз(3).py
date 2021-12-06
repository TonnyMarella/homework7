# Обьявляем 4 функции операций
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if a == 0 or b == 0:
        return "Ошибка! Деление на 0 невозможно"
    else:
        return a / b


# Определяем действие которое будем совершать, и создаём переменную running для зацикливания операции

while True:
    action = input("Введите действие которое вы хотите совершить\n")

    if action == "+":
        a = int(input("Введите значение a\n"))
        b = int(input("Введите значение b\n"))
        print("Ваш результат: ", addition(a, b))

    elif action == "-":
        a = int(input("Введите значение a\n"))
        b = int(input("Введите значение b\n"))
        print("Ваш результат: ", subtraction(a, b))

    elif action == "*":
        a = int(input("Введите значение a\n"))
        b = int(input("Введите значение b\n"))
        print("Ваш результат: ", multiplication(a, b))

    elif action == "/":
        a = int(input("Введите значение a\n"))
        b = int(input("Введите значение b\n"))
        print("Ваш результат: ", division(a, b))

    answer = input("Вы хотите повторить? Введите (y/N)\n").lower()
    if answer != 'y':
        break
