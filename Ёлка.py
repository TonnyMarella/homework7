def elka(x):
    left, right = "/", '\\'
    space = []
    for i in range(x):
        space.append(" ")
    a = list(space)
    del a[0], a[0]
    print(end="{}" "\|/\n""{}-- 0 --\n".format("".join(space), "".join(a)))
    for i in range(x):
        print(end='{}{}|{}\n'.format("".join(space), left, right))
        right += "\\"
        left += "/"
        del space[0]

    a.append("  ")
    print(end="{}""|||\n{}|||".format("".join(a), "".join(a)))


x = int(input("Введите высоту ёлки\n"))
elka(x)
