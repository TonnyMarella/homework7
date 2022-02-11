import requests
from time import time


def get_images(url):
    r = requests.get(url, allow_redirects=True)
    return r


def get_write(response):
    # https://loremflickr.com/cache/resized/65535_51359544383_5623237928_320_240_nofilter.jpg
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    start = time
    url = "https://loremflickr.com/320/240"

    for i in range(10):
        get_write(get_images(url))

    print(time() - start)

if __name__ == '__main__':
    main()