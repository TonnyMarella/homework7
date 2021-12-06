def is_year_leap(year):
    for i in range(0, year+1, 4):
        if i == year:
            return True
    return False


year = int(input("Введите год\n"))

year = is_year_leap(year)

print(year)