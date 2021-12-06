class Temp:
    def __init__(self, cel, fr):
        self.cel = cel
        self.fr = fr
        self.fr_result = (self.cel * 9 / 5) + 32
        self.cel_result = (self.fr - 32) / 1.8000

    def celsius(self):
        print(f"Температура по Цельсию будет равна:{round(self.cel_result, 2)}")

    def forengate(self):
        print(f"Температура по Форенгейту будет равна:{round(self.fr_result, 2)}")


a1 = Temp(-13.00, 5)
a1.forengate()
a1.celsius()
