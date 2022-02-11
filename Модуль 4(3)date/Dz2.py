# Создайте три функции, одна из которых читает файл на диске с заданным именем и проверяет наличие строку “Wow! ”.
# В случае, если файла нет, то засыпает на 5 секунд, а затем снова продолжает поиск по файлу.
# В случае, если файл есть, то открывает его и ищет строку “Wow!”. При наличии данной строки закрывает файл
# и генерирует событие, а другая функция ожидает данное событие и в случае его возникновения выполняет
# удаление этого файла.
# В случае если строки «Wow!» не было найдено в файле, то засыпать на 5 секунд
import asyncio
import os

date = 'Ffasdfasdfasd sdfasdfasdf ssdafasdgadg'
date2 = 'fsdafdsafdsf SFsdfsdfsdf SFDdffdsf Wow!'

with open("file.txt", 'w') as file:
    file.write(date)

with open("file2.txt", 'w') as file:
    file.write(date2)


async def find_wow():
    print("Началась первая функция")
    with open("file.txt", 'r') as file:
        date = file.read().split()
        for i in date:
            if i.lower() == "wow!":
                print("Строка Wow! есть")
                file.close()
                await delete_file(file)
                break
            print('Функция 1 поиска заснула!')  # Если убрать await.sleep с цикла for выполнение будет быстрее
            await asyncio.sleep(5)             # но для наглядности что функции работают поочерёдно я решил оставить так


async def find_wow2():
    print("Началась 2 функция")
    with open("file2.txt", 'r') as file:
        date = file.read().split()
        for i in date:
            if i.lower() == "wow!":
                print("Строка Wow! есть")
                file.close()
                await delete_file(file)
                break
            print('Функция 2 поиска заснула!')
            await asyncio.sleep(5)


async def delete_file(file):
    os.remove(file.name)
    print("Файл", file.name, "удалён!")


async def main():
    loop.create_task(find_wow())
    loop.create_task(find_wow2())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()