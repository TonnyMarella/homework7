from bs4 import BeautifulSoup as BS
import requests
import csv


URL = 'https://auto.ria.com/uk/newauto/category-legkovie/'
LINK = 'https://auto.ria.com/uk/newauto/'
car_page_url = []

r = requests.get(URL)
result = BS(r.text, 'html.parser')
items = result.find_all('section', class_='proposition')

name_car = []
city_car = []
link_car = []
for item in items:
    link_car.append(LINK + item.find('a', class_='proposition_link').get('href'))
    city_car.append(item.find('div', class_='proposition_information').find('span').get('title'))
    name_car.append(item.find('div', class_='proposition_title').find('span').get_text(strip=True))

with open('avtoria.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Название', 'Город', 'Ссылка'])
    for i in range(len(name_car)):
        writer.writerow(name_car[i])