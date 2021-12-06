class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f' Создан Школа Имя {self.name}.')

    def tell(self):
        print(f"Имя {self.name}, возраст {self.age}")


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f"Создан Учитель {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Зарплата {self.salary}")


t1 = Teacher("riba", "pida", 25000)
t1.tell()