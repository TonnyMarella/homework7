# Создайте метакласс, который проверяет класс на запрет использования цифр в именах атрибутов и методах,
# а также верхнего регистра. Генерировать исключение, если данные правила нарушены


class My_metaclass(type):
    def __new__(cls, name, bases, attributes):
        for k, v in attributes.items():
            if isinstance(k, str):
                if not k.islower():
                    raise TypeError("Методы и атрибуты должны быть в нижнем регистре!")
                for i in list(k):
                    if i.isdigit():
                        raise TypeError("Методы и атрибуты должны быть без цифр!")
            else:
                raise TypeError("Методы и атрибуты должны быть в строковом виде!")
        print('In metaclass, creating the class.')
        new_cls = super().__new__(cls, name, bases, attributes)
        return new_cls


class C(metaclass=My_metaclass):
    def __init__(self):
        print('Creating object.')

    def __str__(self):
        return "Str method"


B = My_metaclass("B", (My_metaclass,), {"hello": "world"})

c1 = C()
b1 = B

print(str(c1))
print(b1)
