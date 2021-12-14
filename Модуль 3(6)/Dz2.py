list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = (i ** 2 for i in list1 if i % 2 == 0)

print("Генератор:")
print(next(x), end = ' ')
print(next(x), end = ' ')
print(next(x), end = ' ')
print(next(x), end = ' ')
print(next(x))

print("Цикл:")

for i in list1:
    if i % 2 == 0:
        print(i ** 2, end=' ')


