class Employee:
    def __init__(self, name, second_name, departament, year):
        self.name = name
        self.second_name = second_name
        self.departament = departament
        self.year = year

    special_names = {}

    def __repr__(self):
        person_name = Employee.special_names.get(self.name, str(self.name))
        second_name = Employee.special_names.get(self.second_name, str(self.second_name))
        person_departament = Employee.special_names.get(self.departament, str(self.departament))
        person_year = Employee.special_names.get(self.year, str(self.year))
        return f'Имя: {person_name}, Фамилия: {second_name}, департамент: {person_departament},' \
               f' год поступления: {person_year}'

    @staticmethod
    def add_person():
        add_name = input("Введите имя:\n")
        add_second_name = input("Введите фамилию:\n")
        add_departament = input("Введите депортамент:\n")
        while True:
            try:
                add_year = int(input("Введите год поступления:\n"))
                break
            except ValueError:
                print("Год должен быть числом:\n")
        new_person = Employee(add_name, add_second_name, add_departament, add_year)
        list1.append(new_person)
        for i in list1:
            print(i)

    @staticmethod
    def delete_person():
        delete_name = input("Введите имя для удаления:\n")
        for i in list1:
            person1_name = Employee.special_names.get(i.name, str(i.name))
            if person1_name == delete_name:
                list1.remove(i)
        print(str(list1))

    @staticmethod
    def findPerson():
        find_year = int(input("Введите год: \n"))
        for i in list1:
            person1_year = Employee.special_names.get(i.year, str(i.year))
            if int(person1_year) > int(find_year):
                print(i)


list1 = []
while True:
    x = input("Введите 1 для добавления работника, 2 для удаления, 3 для поиска, 4 для выхода\n")
    if x == "1":
        Employee.add_person()
    if x == "2":
        Employee.delete_person()
    if x == "3":
        Employee.findPerson()
    if x == "4":
        break
