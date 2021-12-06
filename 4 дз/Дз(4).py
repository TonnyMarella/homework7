x = int(input("Укажите ширину прямоугольника\n"))
y = int(input("Укажите высоту прямоугольника\n"))

for i in range(y):
    print()
    for j in range(x):
        print('*', end='')
