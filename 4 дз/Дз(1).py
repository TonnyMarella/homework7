a = int(input("Введите число a\n"))
b = int(input("Введите число b(больше а)\n"))

summ = 0

while a <= b:
    summ += a
    a += 1

print("Сумма =", summ)