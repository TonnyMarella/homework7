import shelve


def get_links(x):
    try:
        with shelve.open("test3") as f:
            print(f[x])
    except KeyError:
        print("Ссылки по данному названию не найдены!")


def add_links(x, y):
    with shelve.open('test3') as f:
        f[y] = x
        print(f"Ссылка: {x}\nУспешно добавлена!")


def get_all_links():
    with shelve.open("test3") as f:
        for key in f:
            print(key, '-', f[key])


def del_links(x):
    with shelve.open("test3") as f:
        del f[x]
        print(f'Ссылка удалена!')