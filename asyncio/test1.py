import requests
import asyncio
import aiohttp
from time import time

#
# async def get_images(url):
#     r = requests.get(url, allow_redirects=True)
#     await r
#
#
# async def get_write(response):
#     # https://loremflickr.com/cache/resized/65535_51359544383_5623237928_320_240_nofilter.jpg
#     filename = response.url.split('/')[-1]
#     with open(filename, 'wb') as file:
#         file.write(response.content)
#
#
# async def main():
#     start = time()
#     url = "https://loremflickr.com/320/240"
#
#     for i in range(10):
#         get_write(get_images(url))
#
#     print(time() - start)
#
#
# if __name__ == '__main__':
#     main()
#

#######################################


def write_image(date):
    filename = "file-{}.jpeg".format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(date)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        date = await response.read()
        write_image(date)


async def main2():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            tasks.append(asyncio.create_task(fetch_content(url, session)))

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = time()
    asyncio.run(main2())
    print(time() - start)