class Zebra:
    def __init__(self):
        self.counter = 1
    def which_stripe(self):
        if self.counter == 1:
            print(f"Полоска белая")
            self.counter += 1
        else:
            print(f"Полоска черная")
            self.counter -= 1

z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
print('-' * 20)
z2 = Zebra()
z2.which_stripe()
z2.which_stripe()
z2.which_stripe()
z2.which_stripe()

