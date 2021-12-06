def season(month):
    if month == 1 or month == 2 or month == 12:
        print("Это месяц зимы")
    elif 2 < month <= 5:
        print("Это месяц весны")
    elif 5 < month <= 8:
        print("Это месяц лета")
    elif 8 < month <= 11:
        print("Это месяц осени")
    else:
        print("Операция некорректная")


x = int(input("Введите номер месяца\n"))

season(x)
