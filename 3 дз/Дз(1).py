name = input("Введите ваше имя:\n")
MyName = str("Artem")

if MyName == name:
    print("Ваше имя совпадает с моим, будем знакомы:)")
elif name.isdigit():
    print("Сомневаюсь что вас так зовут")
else:
    print("Будем знакомы", name, ",меня зовут", MyName)
