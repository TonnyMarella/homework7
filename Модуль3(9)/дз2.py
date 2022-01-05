import time
import shelve

while True:
    a = input("Что вы хотите сделать?\n1. Получить ссылку по названию.\n2. Добавить ссылку с названием."
              "\n3. Посмотреть все доступные ссылки\n4.Удалить сылку\n5.Выйти с программы\n")
    if a == "1":
        x = input("Введите коротное название:\n")
        try:
            with shelve.open("test3") as f:
                print(f[x])
        except KeyError:
            print("Ссылки по данному названию не найдены!")
    elif a == "2":
        with shelve.open('test3') as f:
            x = input("Введите полную ссылку:\n")
            y = input("Введите короткое название на ссылку:\n")
            f[y] = x
            print(f"Ссылка: {x}\nУспешно добавлена!")
    elif a == "3":
        with shelve.open("test3") as f:
            for key in f:
                print(key, '-', f[key])
    elif a == "4":
        with shelve.open("test3") as f:
            x = input("Укажите короткое название сылки которую вы хотите удалить\n")
            del f[x]
    elif a == "5":
        break
    else:
        print("Выберите один из вариантов!")
    time.sleep(2)