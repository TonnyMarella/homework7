list1 = [1, 2, 3, 4, 5]

x = (i for i in list1[::-1])

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))