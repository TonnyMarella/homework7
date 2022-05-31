from bs4 import BeautifulSoup as BS
import requests
import xlsxwriter

model_cars = {
    '1': 'Volkswagen',
    '2': 'Opel',
    '3': 'Audi',
    '4': 'BMW',
    '5': 'Toyota',
    '6': 'Skoda',
    '7': 'Peugeot',
    '8': 'Renault',
    '9': 'Ford',
    '10': 'Mercedes-Benz',
}


def oto_motto(from_price, to_price, od_year, to_year, od_mileage, to_mileage, color='black', name='opel/'):
    name_car = []
    cost_car = []
    link_car = []
    year_car = []
    mileage_car = []
    pages = 1
    page = 1

    r = requests.get("https://www.otomoto.pl/osobowe/" + name + 'od-' + od_year +
                     '?search%5Bfilter_enum_color%5D=' + color +
                     '&search%5Bfilter_float_mileage%3Afrom%5D=' + od_mileage +
                     '&search%5Bfilter_float_price%3Afrom%5D=' + from_price +
                     "&search%5Bfilter_float_price%3Ato%5D=" + to_price +
                     '&search%5Bfilter_float_year%3Ato%5D=' + to_year +
                     '&search%5Bfilter_float_mileage%3Ato%5D=' + to_mileage +
                     '&search%5Bfilter_enum_upholstery_type%5D=upholstery-with-leather'
                     '-inserts&search%5Badvanced_search_expanded%5D=true')
    html = BS(r.content, 'html.parser')

    if html.find_all('div', class_="ooa-1oll9pn e19uumca7"):
        pages = int(html.find_all('div', class_="ooa-1oll9pn e19uumca7")[0].find_all('li')[-2].text)

    while page <= pages:
        print(page)
        r = requests.get("https://www.otomoto.pl/osobowe/" + name + 'od-' + od_year +
                         '?search%5Bfilter_enum_color%5D=' + color +
                         '&search%5Bfilter_float_mileage%3Afrom%5D=' + od_mileage +
                         '&search%5Bfilter_float_price%3Afrom%5D=' + from_price +
                         "&search%5Bfilter_float_price%3Ato%5D=" + to_price +
                         '&search%5Bfilter_float_year%3Ato%5D=' + to_year +
                         '&search%5Bfilter_float_mileage%3Ato%5D=' + to_mileage +
                         '&search%5Bfilter_enum_upholstery_type%5D=upholstery-with-leather'
                         '-inserts&search%5Badvanced_search_expanded%5D=true' +
                         '&page=' + str(page))

        html = BS(r.content, 'html.parser')

        links = html.find_all("h2", class_='e1b25f6f13 ooa-1mgjl0z-Text eu5v0x0')
        cost = html.find_all('div', class_='e1b25f6f9 ooa-1w7uott-Text eu5v0x0')
        years = html.find_all('div', class_='ooa-1nvnpye e1b25f6f5')

        for sum in cost:
            cost_car.append(sum.text[0:6] + " злотых")

        for link in links:
            name_car.append(link.text)
            link_car.append(link.find('a').get('href'))

        for year in years:
            year_car.append(year.find_all('li')[0].text + "год")
            mileage_car.append(year.find_all('li')[1].text)
        page += 1

    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()

    for i in range(0, len(name_car)):
        worksheet.write(f'A{i + 1}', name_car[i])
        worksheet.write(f'B{i + 1}', cost_car[i])
        worksheet.write(f'C{i + 1}', year_car[i])
        worksheet.write(f'D{i + 1}', mileage_car[i])
        worksheet.write(f'E{i + 1}', link_car[i])
    workbook.close()


if __name__ == '__main__':
    mark = input('Выберете марку машины:\n'
                 '1. Volkswagen\n2. Opel\n3. Audi\n4. BMW\n5. Toyota\n6. Skoda\n'
                 '7. Peugeot\n8.Renault\n9.Ford\n10.Mercedes-Benz\n')

    low_price = input('Введите от какой цены:\n')
    high_price = input('Введите до какой цены:\n')

    low_year = input('Введите от какого года:')
    high_year = input('Введите до какого года:')

    low_mileage = input('Введите от какого пробега:')
    high_mileage = input('Введите до какого пробега:')

    oto_motto(name=model_cars[mark] + '/', from_price=low_price, to_price=high_price, od_year=low_year, to_year=high_year,
              od_mileage=low_mileage, to_mileage=high_mileage)
