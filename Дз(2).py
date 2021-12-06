a = int(input("Введите число a\n"))
b = int(input("Введите число b\n"))
x = int(input("Введите число x\n"))

result = True

# Поскольку a не всегда будет меньше чем b, для начала выясняем что меньше a или b
# и только после этого начинаем проверку является ли x по середине
if a < b:
    if x <= a:
       result = False
       print("Ваш результат:", result)
    elif x >= b:
       result = False
       print("Ваш результат:", result)
    else:
       print("Ваш результат:", result)
elif b < a:
    if x >= a:
        result = False
        print("Ваш результат:", result)
    elif x <= b:
        result = False
        print("Ваш результат:", result)
    else:
        print("Ваш результат:", result)