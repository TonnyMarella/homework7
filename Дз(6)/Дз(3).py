def ladder(step):
    a = 1
    b = 2
    c = 0

    for i in range(2, step):
        c = a + b
        a = b
        b = c

    print("Способов забраться на", step, "cтупеньку =", c)


x = int(input("Введите на какую ступеньку вы хотите подняться\n"))

if x == 1:
    print("Количество способов = 1")
elif x == 2:
    print("Количество способов = 2")
else:
    ladder(x)
