a = int(input("Введите 1 промежуток\n"))
b = int(input("Введите 2 промежуток\n"))

x = []

for i in range(a, b+1):
    x.append(i)

result = sum(x)

print("Сумма чисел от 1 промежутка до 2 =", result)
