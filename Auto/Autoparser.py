from bs4 import BeautifulSoup as BS
from const import model_cars_otto, model_cars_mobile
import requests
import xlsxwriter


def oto_motto(from_price, to_price, od_year, to_year, od_mileage, to_mileage, color='black', name='opel'):
    from_price = str(int(from_price * 4.32))
    to_price = str(int(to_price * 4.32))
    car_name = []
    car_price = []
    car_link = []
    car_year = []
    car_mileage = []
    pages = 1
    page = 1

    URL = "https://www.otomoto.pl/osobowe/" + name + "/od-" + od_year +\
          "?search%5Bfilter_float_year%3Ato%5D=" + to_year +\
          "&search%5Bfilter_float_mileage%3Afrom%5D=" + od_mileage +\
          "&search%5Bfilter_float_price%3Afrom%5D=" + from_price +\
          "&search%5Bfilter_float_price%3Ato%5D=" + to_price +\
          "&search%5Bfilter_float_mileage%3Ato%5D=" + to_mileage +\
          "&search%5Bfilter_enum_upholstery_type%5D=upholstery-with-leather-inserts"\
          "&search%5Bfilter_enum_color%5D=" + color

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/101.0.4951.67 Safari/537.36'}

    r = requests.get(URL, headers=headers)
    html = BS(r.content, 'html.parser')

    if html.find_all('div', class_="ooa-1oll9pn e19uumca7"):
        pages = int(html.find_all('div', class_="ooa-1oll9pn e19uumca7")[0].find_all('li')[-2].text)

    while page <= pages:
        print('otto', page)
        r = requests.get(URL + "&page=" + str(page), headers=headers)

        html = BS(r.content, 'html.parser')
        print(URL)

        car_date = html.find_all('article', class_='ooa-rld5ij e1b25f6f18')

        for date in car_date:
            car_name.append(date.find('a').text)
            car_link.append(date.find('a').get('href'))
            car_price.append(date.find('span', class_='ooa-epvm6 e1b25f6f8').text)
            car_year.append(date.find('ul').text[:4] + ' год')
            car_mileage.append(date.find('ul').text[5: 12] + ' км')

        print('otto', car_name)
        page += 1

    return [car_name, car_link, car_price, car_year, car_mileage]


def mobile(from_price, to_price, od_year, to_year, od_mileage, to_mileage, color='BLACK', name='19000'):
    from_price = str(int(from_price * 1.06))
    to_price = str(int(to_price * 1.06))

    car_name = []
    car_price = []
    car_link = []
    car_year = []
    car_mileage = []
    pages = 1
    page = 1

    URL = 'https://suchen.mobile.de/fahrzeuge/search.html'\
          '?fr=' + od_year + '%3A' + to_year + '&isSearchRequest=true''&ml=' + od_mileage + \
          '%3A' + to_mileage + '&ms=' + name + '%3B%3B%3B%3B&it=PARTIAL_LEATHER&p=' + from_price + '%3A' + to_price + \
          '&ref=srp&refId=9304704f-45d6-64c8-fbf1-3dbe9597f523&s=Car&sb=rel&sfmr=false&vc=Car&ecol=' + color

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/101.0.4951.67 Safari/537.36'}

    r = requests.get(URL, headers=headers)

    html = BS(r.content, 'html.parser')

    if html.find_all('ul', class_="pagination"):
        pages = int(html.find_all('span', class_='btn btn--secondary btn--l')[-1].text)

    while page <= pages:
        print('mobile: ', page)
        r = requests.get(URL + 'pageNumber=' + str(page), headers=headers)

        html = BS(r.content, 'html.parser')

        car_date = html.find_all('div', class_='cBox-body cBox-body--resultitem')

        for date in car_date:
            car_name.append(date.find('span', class_='h3 u-text-break-word').text)
            car_link.append(date.find('a').get('href'))
            car_price.append(date.find('span', class_='h3 u-block').text[:-2] + ' евро')
            car_year.append(date.find('div', class_='vehicle-data--ad-with-price-rating-label').text[3:10])
            car_mileage.append(date.find('div', class_='vehicle-data--ad-with-price-rating-label').text[12:21])

        page += 1

    return [car_name, car_link, car_price, car_year, car_mileage]


def gidas(from_price, to_price, od_year, to_year, od_mileage, to_mileage, name='opel'):
    from_price = str(int(from_price * 1.06))
    to_price = str(int(to_price * 1.06))

    car_name = []
    car_price = []
    car_link = []
    car_year = []
    car_mileage = []
    pages = 1
    page = 1

    URL = "https://autogidas.lt/ru/skelbimai/automobiliai/" \
          "?f_215=" + from_price + "&f_216=" + to_price + \
          "&f_41=" + od_year + "&f_42=" + to_year + \
          "&f_65=" + od_mileage + "&f_66=" + to_mileage + "&f_5=Juoda&a_18=1&s=1372972183&f_1%5B0%5D=" + name

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/101.0.4951.67 Safari/537.36'}

    r = requests.get(URL, headers=headers)

    html = BS(r.content, 'html.parser')

    if html.find_all('div', class_="pagination"):
        pages = int(html.find_all('div', class_='paginator')[0].text[-5:].replace(' ', ''))

    while page <= pages:
        print('gidas: ', page)

        r = requests.get(URL + "&page=" + str(page), headers=headers)
        html = BS(r.content, 'html.parser')
        print(URL)

        car_date = html.find_all('article', class_='list-item')

        for date in car_date:
            car_name.append(date.find('h2', class_='item-title').text)
            car_link.append('https://autogidas.lt/' + date.find('a').get('href'))
            car_price.append(date.find('div', class_='item-price').text.replace(' ', ''))
            car_year.append(date.find('div', class_='primary').text[:-20])
            car_mileage.append(date.find('div', class_='secondary').text[:-20])

        print('gidas', car_name)

        page += 1

    return [car_name, car_link, car_price, car_year, car_mileage]


if __name__ == '__main__':
    mark = input('Выберете марку машины(Написать марку):\n'
                 '1. Volkswagen\n2. Opel\n3. Audi\n4. BMW\n5. Toyota\n6. Skoda\n'
                 '7. Peugeot\n8.Renault\n9.Ford\n10.Mercedes-Benz\n')

    low_price = float(input('Введите от какой цены(доллары):\n'))
    high_price = float(input('Введите до какой цены(доллары):\n'))

    low_year = input('Введите от какого года:')
    high_year = input('Введите до какого года:')

    low_mileage = input('Введите от какого пробега:')
    high_mileage = input('Введите до какого пробега:')

    name_car, link_car, cost_car, year_car, mileage_car = oto_motto(
        name=model_cars_otto[mark],
        from_price=low_price, to_price=high_price, od_year=low_year,
        to_year=high_year, od_mileage=low_mileage, to_mileage=high_mileage)

    name_car2, link_car2, cost_car2, year_car2, mileage_car2 = mobile(
        name=model_cars_mobile[mark], from_price=low_price, to_price=high_price,
        od_year=low_year, to_year=high_year,
        od_mileage=low_mileage, to_mileage=high_mileage)

    name_car3, link_car3, cost_car3, year_car3, mileage_car3 = gidas(
        name=model_cars_otto[mark],
        from_price=low_price, to_price=high_price, od_year=low_year,
        to_year=high_year, od_mileage=low_mileage, to_mileage=high_mileage)

    name_car += name_car2 + name_car3
    link_car += link_car2 + link_car3
    cost_car += cost_car2 + cost_car3
    year_car += year_car2 + year_car3
    mileage_car += mileage_car2 + mileage_car3

    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()

    for i in range(0, len(name_car)):
        worksheet.write(f'A{i + 1}', name_car[i])
        worksheet.write(f'B{i + 1}', cost_car[i])
        worksheet.write(f'C{i + 1}', year_car[i])
        worksheet.write(f'D{i + 1}', mileage_car[i])
        worksheet.write(f'E{i + 1}', link_car[i])

    workbook.close()
