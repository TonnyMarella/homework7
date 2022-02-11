import numpy as np
from random import randint

lst = []

for i in range(180):
    lst.append(randint(15, 30))

arr = np.array(lst, "int8").reshape(6, 30)

june = arr[0].reshape(15, 2)
new_june = np.append(june, arr[1]).reshape(30, 2)
print("Температура в Июне:")
for i in new_june:
    print("День:", i[0], "------", i[1], "Ночь")
print("В Июне, самая большая температура ровнялась:", june.max(), "\nЭто было в", int(june.argmax() / 2) + 1, "дне")

july = arr[2].reshape(15, 2)
new_july = np.append(june, arr[3]).reshape(30, 2)
print("Температура в Июле:")
for i in new_july:
    print("День:", i[0], "------", i[1], "Ночь")
print("В Июле, самая большая температура ровнялась:", june.max(), "\nЭто было в", int(june.argmax() / 2) + 1, "дне")

august = arr[2].reshape(15, 2)
new_august = np.append(june, arr[3]).reshape(30, 2)
print("Температура в Августе:")
for i in new_august:
    print("День:", i[0], "------", i[1], "Ночь")
print("В Августе, самая большая температура ровнялась:", june.max(), "\nЭто было в", int(june.argmax() / 2) + 1, "дне")


file_arr = np.array([new_june[-1][0], new_june[-1][1], new_june[-2][0], new_june[-2][1], new_june[-3][0],
                    new_july[-1][0], new_july[-1][1], new_july[-2][0], new_july[-2][1], new_july[-3][0],
                    new_august[-1][0], new_august[-1][1], new_august[-2][0], new_august[-2][1],
                     new_august[-3][0]]).reshape(3, 5)

with open("file.txt", "w") as file:
    file.write(str(file_arr))