class Quadrilateral:
    def __init__(self, *args):
        self.width = args[0]
        self.height = args[-1]

    def __str__(self):
        if self.width == self.height:
            return f'Куб размером {self.width}х{self.height}'
        return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.height == self.width


q1 = Quadrilateral(10, 10)
print(q1)
print(bool(q1))
q2 = Quadrilateral(3, 5)
print(q2)
print(q2 == True)
q3 = Quadrilateral(50, 50)
print(q3)
print(bool(q3))