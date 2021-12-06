def expenses(computer, monitor, keyboard, mouse, mfu, switch):
    a = computer * 27862
    print("Стоимость", computer, "компьютеров составляет: ", a, "грн")
    b = monitor * 7499
    print("Стоимость", monitor, "монитров составляет: ", b, "грн")
    c = keyboard * 867
    print("Стоимость", keyboard, "клавиатур составляет: ", c, "грн")
    d = mouse * 437
    print("Стоимость", mouse, "мышек составляет: ", d, "грн")
    f = mfu * 10124
    print("Стоимость", mfu, "МФУ составляет: ", f, "грн")
    s = switch * 6253
    print("Стоимость", switch, "коммутаторов составляет: ", s, "грн")
    summ = a + b + c + d + f + s
    print("Общая стоимость всего составляет:", summ)


expenses(15, 20, 15, 15, 5, 1)
