class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @property
    def cents(self):
        return self.total_cents % 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value > 0:
            self.total_cents = value * 100 + self.cents
        else:
            print("Error dollars")

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 0 < value < 100:
            self.total_cents = value * 100 + self.cents
        else:
            print("Error cents")

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов'"


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов


