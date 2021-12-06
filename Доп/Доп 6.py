def skolko(panel, metr1, metr2):
    kvadrat = metr1 * metr2
    kvadrat *= 2
    print("Одна панель это:", kvadrat, "метров квадратных")
    print("Для ремонта", panel, " панелей, потребуется:")

    panel *= kvadrat

    print(panel, "Сульфида")


a = int(input("Введите количестко панелей\n"))
b = int(input("Введите сколько метров панель в высоту\n"))
c = int(input("Введите сколько метров панель в ширину\n"))

skolko(a, b, c)
