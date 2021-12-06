class Money:
    TOTAL_CENTS = 0

    def __init__(self, dollars, cent):
        self.dollars = dollars
        self.cent = cent
        Money.TOTAL_CENTS += cent

    @property
    def all_dollars(self):
        return self.dollars

    @all_dollars.setter
    def all_dollars(self, value):
        self.value = value
        if self.value < 0:
            print(f"Error dollars")
        else:
            self.dollars += self.value

    @property
    def all_cent(self):
        return self.cent

    @all_cent.setter
    def all_cent(self, value):
        self.value = value
        if 0 < self.value > 100:
            print(f"Error cents")
        else:
            Money.TOTAL_CENTS += self.value

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {Money.TOTAL_CENTS} центов"

Bill = Money(101, 99)
Bill.dollars = 500

Money.