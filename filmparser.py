import requests
from bs4 import BeautifulSoup as bs


URL = 'https://rezka.ag/films/'

r = requests.get(URL)

result = bs(r.text, 'html.parser')
items = result.find_all('div', class_='b-content__inline_item')

print(result)