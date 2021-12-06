def palindrom(word):
    print(word[::-1])
    if word == word[::-1]:
        print('Является палиндромом')
    else:
        print('Не является палиндромом')


x = input('Введите слово: ').lower()
palindrom(x)
