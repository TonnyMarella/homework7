class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            if self.rating == other:
                return True
            else:
                return False
        elif isinstance(other, ChessPlayer):
            if self.rating == other.rating:
                return True
            else:
                return False
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, int):
            if self.rating > other:
                return True
            else:
                return False
        elif isinstance(other, ChessPlayer):
            if self.rating > other.rating:
                return True
            else:
                return False
        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, int):
            if self.rating < other:
                return True
            else:
                return False
        elif isinstance(other, ChessPlayer):
            if self.rating < other.rating:
                return True
            else:
                return False
        else:
            return 'Невозможно выполнить сравнение'




magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000)
print(ian == 2789)
print(magnus == ian)
print(magnus > ian)
print(magnus < ian)
print(magnus < [1, 2])