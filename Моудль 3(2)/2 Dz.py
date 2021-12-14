class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return f'Высота {self.height}, ширина {self.width}'


class Click:
    @staticmethod
    def click_left():
        return 'Left button clicked'

    @staticmethod
    def click_right():
        return 'Right button clicked'


class Button(Rectangle, Click):
        def __init__(self, height, width, click):
            super().__init__(height, width)
            self.click = click

        def __str__(self):
            return f'"{self.click}" ' + super().__str__()


rec = Rectangle(20, 5)
but = Button(60, 18, 'Ok')
print('Rectangle', rec)
print("-" * 10)
print('Button', but)
print("-" * 10)
print(but.click_left())
print(but.click_right())
