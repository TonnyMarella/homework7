class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, value):
        if isinstance(value, Point): # s = ((x2-x1)**2+(y2-y1)**2)**0.5
            return ((self.x - value.x) ** 2 + (self.y - value.y) ** 2) ** 0,5
        else:
            print("Передана не точка")


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2) # вернёт 5.0
p1.get_distance(10) # Распечатает "Передана не точка"