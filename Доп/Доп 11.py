def bank(contribution, years):
    for i in range(years):
        contribution *= 1.1

    return contribution


a = int(input("Введите сумму на которую вы хотите сделать вклад\n"))
y = int(input("На сколько лет вы хотите сделать данный вклад\n"))

result = bank(a, y)

print("По истечению данного срока вы получите свои деньги размером в:", round(result, 2))
print("Это на", round(result - a, 2), "больше чем вы изначально сделали вклад")
