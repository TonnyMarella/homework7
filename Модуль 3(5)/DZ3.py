list1 = [1, 2, 3, 4, 5]
iterable = iter(list1)
x = []

for i in iterable:
    x.append(i)

print(x[::-1])