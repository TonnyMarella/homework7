import requests
from bs4 import BeautifulSoup as BS
r = requests.get("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2")
html = BS(r.content, 'html.parser')
for el in html.select('#content'):
    t_min = el.select(".temperature")[0].text
    print(t_min)
    t_max = el.select(".temperature .max")[0].text
    print((t_max))

