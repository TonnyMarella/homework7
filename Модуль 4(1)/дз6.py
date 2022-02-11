# Поработать с requests, использовать сайт jsonplaceholder
# Я с помощью get достал всё в текстовом виде с сайта и загрузил это в json файл

import requests
import json


response = requests.get("https://jsonplaceholder.typicode.com/posts")

with open("dz4.json", "w") as file:
    json.dump(response.text, file, indent=4)

with open("dz4.json", "r") as file:
    date = json.load(file)
    print(date)