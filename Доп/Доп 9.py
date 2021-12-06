def square(x):
    p = x * 4
    s = x * 2
    d = x * (2 ** 0.5)
    result = (p, s, d)
    return result


a = int(input("Введите сторону\n"))
result = square(a)
print("Периметр:", result[0], "\nПлощадь:", result[1], "\nДиагональ:", result[2])
