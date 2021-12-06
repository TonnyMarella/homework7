n = int(input("Введите число n\n"))
i = 2
fac = 1
while i < n + 1:
    fac *= i
    i += 1
print("Результат вашего факториала:", fac)