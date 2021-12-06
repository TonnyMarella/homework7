class Vector:
    def __init__(self, *args):
        self.args = list(args)
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)
        self.values.sort()

    def __str__(self):
        if self.values:
            return f"Вектор {tuple(self.values)}"
        else:
            return "Пустой вектор"

    def __add__(self, other):
        new_v = []
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_v.append(self.values[i] + other.values[i])
                return Vector(*[i for i in new_v])
            else:
                print('Сложение векторов разной длины недопустимо')
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_v.append(self.values[i] + other)
            return Vector(*[i for i in new_v])
        if not isinstance(other, (Vector, int)):
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        new_v = []
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_v.append(self.values[i] * other.values[i])
                return Vector(*[i for i in new_v])
            else:
                print('Умножение векторов разной длины недопустимо')
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_v.append(self.values[i] * other)
            return Vector(*[i for i in new_v])
        else:
            print(f'Вектор нельзя умножать с {other}')


v1 = Vector(1,2,3)
print(v1)
v2 = Vector(3,4,5)
print(v2)
v3 = v1 + v2
print(v3)
v4 = v3 + 5
print(v4)
v5 = v1 * 2
print(v5)
v5 + 'hi'