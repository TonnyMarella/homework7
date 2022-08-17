from bs4 import BeautifulSoup as BS
from const import marks_cars_otto, marks_cars_mobile
from abc import ABC, abstractmethod
import xlsxwriter
import requests


class AbstractAutoParser(ABC):
    car_name = []
    car_price = []
    car_link = []
    car_year = []
    car_mileage = []

    def __init__(self):
        super().__init__()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                          ' AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/101.0.4951.67 Safari/537.36'}

    @abstractmethod
    def parser(self):
        pass

    @abstractmethod
    def save_car_date(self):
        pass


class MobileParser(AbstractAutoParser):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.pages = 1
        self.page = 1

    def parser(self):
        r = requests.get(self.url, headers=self.headers)
        html = BS(r.content, 'html.parser')

        if html.find_all('ul', class_="pagination"):
            self.pages = int(html.find_all(
                'span', class_='btn btn--secondary btn--l')[-1].text)

    def save_car_date(self):
        while self.page <= self.pages:
            print('mobile: ', self.page)
            r = requests.get(self.url + 'pageNumber=' + str(self.page),
                             headers=self.headers)

            html = BS(r.content, 'html.parser')

            car_date = html.find_all('div',
                                     class_='cBox-body cBox-body--resultitem')

            for date in car_date:
                AbstractAutoParser.car_name.append(
                    date.find('span', class_='h3 u-text-break-word').text)
                AbstractAutoParser.car_link.append(
                    date.find('a').get('href'))
                AbstractAutoParser.car_price.append(
                    date.find('span', class_='h3 u-block').text[:-2] + ' евро')
                AbstractAutoParser.car_year.append(
                    date.find('div', class_='vehicle-data--ad-with-price-rating-label').text[3:10])
                AbstractAutoParser.car_mileage.append(
                    date.find('div', class_='vehicle-data--ad-with-price-rating-label').text[12:19])

            self.page += 1


class GidasParser(AbstractAutoParser):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.pages = 1
        self.page = 1

    def parser(self):
        r = requests.get(self.url, headers=self.headers)
        html = BS(r.content, 'html.parser')
        if html.find_all('div', class_="pagination"):
            self.pages = int(html.find_all(
                'div', class_='paginator')[0].text[-5:].replace(' ', ''))

    def save_car_date(self):
        while self.page <= self.pages:
            print('gidas: ', self.page)

            r = requests.get(
                self.url + "&page=" + str(self.page), headers=self.headers)
            html = BS(r.content, 'html.parser')

            car_date = html.find_all('article', class_='list-item')

            for date in car_date:
                AbstractAutoParser.car_name.append(
                    date.find('h2', class_='item-title').text)
                AbstractAutoParser.car_link.append(
                    'https://autogidas.lt/' + date.find('a').get('href'))
                AbstractAutoParser.car_price.append(
                    date.find('div', class_='item-price').text.replace(' ', ''))
                AbstractAutoParser.car_year.append(
                    date.find('div', class_='primary').text[:-20])
                AbstractAutoParser.car_mileage.append(
                    date.find('div', class_='secondary').text[:-20])

            self.page += 1


class OttoParser(AbstractAutoParser):
    def __init__(self, url, model_car):
        super().__init__()
        self.model_car = model_car
        self.url = url
        self.pages = 1
        self.page = 1

    def parser(self):
        r = requests.get(self.url, headers=self.headers)
        html = BS(r.content, 'html.parser')

        if html.find_all('div', class_="ooa-1oll9pn e19uumca7"):
            self.pages = int(html.find_all(
                'div', class_="ooa-1oll9pn e19uumca7")[0].find_all('li')[-2].text)

    def save_car_date(self):
        while self.page <= self.pages:
            print('otto', self.page)
            r = requests.get(self.url + "&page=" +
                             str(self.page), headers=self.headers)

            html = BS(r.content, 'html.parser')

            car_date = html.find_all('article',
                                     class_='ooa-rld5ij e1b25f6f18')

            for date in car_date:
                if date.find('a').text.lower().count(self.model_car) == 0:
                    continue

                AbstractAutoParser.car_name.append(
                    date.find('a').text)
                AbstractAutoParser.car_link.append(
                    date.find('a').get('href'))
                AbstractAutoParser.car_price.append(
                    date.find('span', class_='ooa-epvm6 e1b25f6f8').text)
                AbstractAutoParser.car_year.append(
                    date.find('ul').text[:4] + ' год')
                AbstractAutoParser.car_mileage.append(
                    date.find('ul').text[5: 12] + ' км')

            self.page += 1


def save_date():
    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()

    for i in range(0, len(AbstractAutoParser.car_name)):
        worksheet.write(f'A{i + 1}', AbstractAutoParser.car_name[i])
        worksheet.write(f'B{i + 1}', AbstractAutoParser.car_price[i])
        worksheet.write(f'C{i + 1}', AbstractAutoParser.car_year[i])
        worksheet.write(f'D{i + 1}', AbstractAutoParser.car_mileage[i])
        worksheet.write(f'E{i + 1}', AbstractAutoParser.car_link[i])

    workbook.close()


if __name__ == '__main__':
    mark = input('Выберете марку машины(Написать марку):\n'
                 '1. Volkswagen\n2. Opel\n'
                 '3. Audi\n4. BMW\n'
                 '5. Toyota\n6. Skoda\n'
                 '7. Peugeot\n8.Renault\n'
                 '9.Ford\n10.Mercedes-Benz\n')

    start_price_euro = input('Введите от какой цены(евро(мин 150)):\n')
    end_price_euro = input('Введите до какой цены(евро):\n')

    start_price_zlot = input('Введите от какой цены(злоты(мин 2000):\n')
    end_price_zlot = input('Введите до какой цены(злоты):\n')

    start_year = input('Введите от какого года:')
    end_year = input('Введите до какого года:')

    start_mileage = input('Введите от какого пробега:')
    end_mileage = input('Введите до какого пробега:')

    URL_MOBILE = 'https://suchen.mobile.de/fahrzeuge/search.html' \
                 '?fr=' + start_year + '%3A' + end_year + \
                 '&isSearchRequest=true''&ml=' + start_mileage + \
                 '%3A' + end_mileage + '&ms=' + marks_cars_mobile[mark] + \
                 '%3B%3B%3B%3B&it=PARTIAL_LEATHER&p=' + \
                 end_price_euro + '%3A' + start_price_euro + \
                 '&ref=srp&refId=9304704f-45d6-64c8-fbf1-3dbe9597f523&s=Car' \
                 '&sb=rel&sfmr=false&vc=Car&ecol=BLACK'

    URL_GIDAS = "https://autogidas.lt/ru/skelbimai/automobiliai/" \
                "?f_215=" + start_price_euro + "&f_216=" + end_price_euro + \
                "&f_41=" + start_year + "&f_42=" + end_year + \
                "&f_65=" + start_mileage + "&f_66=" + end_mileage + \
                "&f_5=Juoda&a_18=1&s=1372972183&f_1%5B0%5D=" + \
                marks_cars_otto[mark].title()

    URL_OTTO = 'https://www.otomoto.pl/osobowe/' + marks_cars_otto[mark] + \
               '/od-' + start_year + \
               '?search%5Bfilter_enum_upholstery_type%5D=upholstery-with-leather-inserts' \
               '&search%5Bfilter_float_year%3Ato%5D=' + end_year + \
               '&search%5Bfilter_float_mileage%3Afrom%5D=' + start_mileage + \
               '&search%5Bfilter_float_mileage%3Ato%5D=' + end_mileage + \
               '&search%5Bfilter_float_price%3Afrom%5D=' + start_price_zlot + \
               '&search%5Bfilter_float_price%3Ato%5D=' + end_price_zlot + \
               "&search%5Bfilter_enum_color%5D=black"

    mobile = MobileParser(URL_MOBILE)
    gidas = GidasParser(URL_GIDAS)
    otto = OttoParser(URL_OTTO, marks_cars_otto[mark])

    mobile.parser()
    mobile.save_car_date()

    gidas.parser()
    gidas.save_car_date()

    otto.parser()
    otto.save_car_date()

    save_date()
