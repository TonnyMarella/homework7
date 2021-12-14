def generator(value):
    for i in range(2, value + 1):
        counter = True
        for y in range(2, i):
            if i % y == 0:
                counter = False
        if counter:
            yield i


x = generator(17)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
