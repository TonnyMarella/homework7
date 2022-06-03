from bs4 import BeautifulSoup as BS
import requests
import xlsxwriter

model_cars_mobile = {
    '1': '25200',
    '2': '19000',
    '3': '1900',
    '4': '3500',
    '5': '24100',
    '6': '22900',
    '7': '19300',
    '8': '20700',
    '9': '9000',
    '10': '17200',
}

# model_cars = {
#     '1': 'Volkswagen',
#     '2': 'Opel',
#     '3': 'Audi',
#     '4': 'BMW',
#     '5': 'Toyota',
#     '6': 'Skoda',
#     '7': 'Peugeot',
#     '8': 'Renault',
#     '9': 'Ford',
#     '10': 'Mercedes-Benz',
# }


def mobile(from_price, to_price, od_year, to_year, od_mileage, to_mileage, color='BLACK', name='19000'):
    name_car = []
    cost_car = []
    link_car = []
    year_car = []
    mileage_car = []
    pages = 1
    page = 1

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/101.0.4951.67 Safari/537.36'}

    r = requests.get('https://suchen.mobile.de/fahrzeuge/search.html'
                     '?fr=' + od_year + '%3A' + to_year + '&isSearchRequest=true'
                     '&ml=' + od_mileage + '%3A' + to_mileage + '&ms=' + name + '%3B%3B%3B%3B'
                     '&p=' + from_price + '%3A' + to_price + '&ref=srp&refId=9304704f-45d6-64c8-fbf1-3dbe9597f523'
                     '&s=Car&sb=rel&sfmr=false&vc=Car&ecol=' + color, headers=headers)

    html = BS(r.content, 'html.parser')

    if html.find_all('ul', class_="pagination"):
        pages = int(html.find_all('span', class_='btn btn--secondary btn--l')[-1].text)

    while page <= pages:
        print(page)
        r = requests.get('https://suchen.mobile.de/fahrzeuge/search.html'
                         '?fr=' + od_year + '%3A' + to_year + '&isSearchRequest=true'
                         '&ml=' + od_mileage + '%3A' + to_mileage + '&ms=' + name + '%3B%3B%3B%3B'
                         '&p=' + from_price + '%3A' + to_price + '&ref=srp&refId=9304704f-45d6-64c8-fbf1-3dbe9597f523'
                         '&s=Car&sb=rel&sfmr=false&vc=Car&ecol=' + color + 'pageNumber=' + str(page),
                         headers=headers)

        html = BS(r.content, 'html.parser')

        car_date = html.find_all('div', class_='cBox-body cBox-body--resultitem')

        for date in car_date:
            name_car.append(date.find('span', class_='h3 u-text-break-word').text)
            link_car.append(date.find('a').get('href'))
            cost_car.append(date.find('span', class_='h3 u-block').text[:-2] + ' евро')
            year_car.append(date.find('div', class_='vehicle-data--ad-with-price-rating-label').text[3:10])
            mileage_car.append(date.find('div', class_='vehicle-data--ad-with-price-rating-label').text[12:18] + ' км')

        page += 1
    return [name_car, link_car, cost_car, year_car, mileage_car]

    # workbook = xlsxwriter.Workbook('hello.xlsx')
    # worksheet = workbook.add_worksheet()
    #
    # for i in range(0, len(name_car)):
    #     worksheet.write(f'A{i + 1}', name_car[i])
    #     worksheet.write(f'B{i + 1}', cost_car[i])
    #     worksheet.write(f'C{i + 1}', year_car[i])
    #     worksheet.write(f'D{i + 1}', mileage_car[i])
    #     worksheet.write(f'E{i + 1}', link_car[i])
    # workbook.close()


name_car, link_car, cost_car, year_car, mileage_car = mobile(name='19000', from_price='4000', to_price='6000', od_year='2008', to_year='2015',
                                                            od_mileage='50000', to_mileage='60000')

print(mileage_car)