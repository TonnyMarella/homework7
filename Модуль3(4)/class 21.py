class Wallet:
    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        elif len(currency) != 3:
            raise NameError("Неверная длина названия валюты")
        elif not currency.isupper():
            raise ValueError("Название должно состоять только из заглавных букв")
        elif not isinstance(balance, int):
            raise ValueError("Здесь должны быть цифры")
        else:
            self.currency = currency
            self.balance = balance

    def __eq__(self, other):
        if other.currency != self.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        elif not isinstance(other, Wallet):
            raise TypeError(f"Wallet не поддерживает сравнение с {other}")
        return self.balance == other.balance

    def __add__(self, other):
        if other.currency != self.currency:
            raise ValueError("Данная операция запрещена")
        elif not isinstance(other, Wallet):
            raise ValueError("Данная операция запрещена")
        else:
            return Wallet(other.currency, self.balance + other.balance)

    def __sub__(self, other):
        if other.currency != self.currency:
            raise ValueError("Данная операция запрещена")
        elif not isinstance(other, Wallet):
            raise ValueError("Данная операция запрещена")
        else:
            return Wallet(other.currency, self.balance - other.balance)

