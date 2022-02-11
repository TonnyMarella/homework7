# Создайте функцию, которая создает класс, на основе переданных ей названия, атрибутов и методов.
# Необходимо, чтобы все названия переданных атрибутов и методов были приведены к нижнему регистру до создания класса.

def get_first_name(self):
    return self.first_name


def get_second_name(self):
    return self.second_name


def init(self, first_name, second_name):
    self.first_name = first_name
    self.second_name = second_name


class BaseUser:
    def __str__(self):
        return '<user-object/>'


def create_class(class_name, parents, attributes):
    print('In funchion, creating the class.')
    return type(class_name, parents, attributes)


attr = {
    "first name": "",
    "Second name": "",
    "Get_First_name": get_first_name,
    "Get_Second_name": get_second_name,
    "__init__": init
}
new_attr = dict((k.lower() if isinstance(k, str) else
                 k, v.lower() if isinstance(v, str) else v) for k, v in attr.items())


User = create_class("Created_User", (BaseUser, ), new_attr)
user1 = User("Alex", " Volchanov")
user2 = User("Dmitriy", "Gubernev")

print(user1.get_first_name())
print(user2.get_second_name())
