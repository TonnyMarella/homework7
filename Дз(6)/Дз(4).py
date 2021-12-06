def recursion(a):
    if a < n:
        return 0
    else:
        return a + recursion(a - 1)


n = int(input("Введите 1 промежуток\n"))
a = int(input("Введите 2 промежуток\n"))

result = recursion(a)

print("Сумма чисел от 1 промежутка до 2 =", result)
