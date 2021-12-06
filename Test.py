class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'Создан Школа Имя {self.name}.')

    def tell(self):
        print(f"Имя {self.name}, возраст {self.age}, ", end="")


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f"Создан Учитель {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Зарплата {self.salary}")


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f"Создан ученик {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Оценка {self.marks}")


t1 = Teacher("Tolik", "25", 25000)
s1 = Student("Dima", "17", 10)
s2 = Student("Я", "17", 10)

members = [t1, s1, s2]

for i in members:
    i.tell()