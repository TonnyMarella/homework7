x = int(input("Введите количество чисел:\n"))
list1 = []
print("Введите числа:")
for _ in range(x):
    list1.append(int(input()))

print(sorted(list1))
