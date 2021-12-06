def func(a, b):
    return (a + b) * 3 * (a ** b) - 6 * (b ** 2)


a = int(input("Введите 1 число\n"))
b = int(input("Введите 2 число\n"))

result = func(a, b)

print("Результат: ", result)
