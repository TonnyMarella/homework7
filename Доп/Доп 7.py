def arithmetic(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if a == 0 or b == 0:
            return 0
        else:
            return a / b
    else:
        return 0


def main():
    operation = input("Введите операцию которую вы хотите совершить\n")
    a = int(input("Введите первое числo\n"))
    b = int(input("Введите второе число\n"))
    x = arithmetic(a, b, operation)

    if x == 0:
        print("Неизвестная операция")
    else:
        print("Результат:", x)


if __name__ == '__main__':
    main()