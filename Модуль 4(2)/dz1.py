# Создайте простые словари и сконвертируйте их в JSON. Сохраните JSON в файл и попробуйте загрузить данные из файла.
import json

simple_dict = {
    "1": 232,
    "2": "212",
    "3": "New-York"
}


with open("first.json", 'w') as file:
    json.dump(simple_dict, file, indent=3)

with open('first.json', 'r') as file:
    date = json.load(file)
    print(date)


