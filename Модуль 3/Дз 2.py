class Book:
    LIST_REVIEW = []

    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f'Автор {self.author}, книга {self.name}'

    def __str__(self):
        return f'Автор {self.author}, книга {self.name}, год издания {self.year}, жанр {self.genre}, ' \
               f'\nСписок отзывов:\n{Book.LIST_REVIEW}'

    def __eq__(self, other):
        if (self.author, self.name, self.year, self.genre) == (other.author,
                                                               other.name, other.year, other.genre):
            return True
        return False


class Review:
    def __init__(self, *args):
        self.text = args
        Book.LIST_REVIEW = self.text


r1 = Review("10/10", "9/10", "8/10")
b1 = Book("Дмитрий Глуховский", "Метро 2033", "2005", "Роман, научная фантастика")
b2 = Book("Рафаэлло Джованьоли", "Спартак", "1874", "Исторический роман")

print(b1)
print(b1 == b2)
