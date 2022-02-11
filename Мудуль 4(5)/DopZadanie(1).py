# Задание 1
# Создайте двухмерный массив размерностью 25 x 25 и умножьте его на единичную матрицу.

import numpy as np

print("Начало 1 задания!")
a = list(range(1, 26))

arr = np.array([a, a])
arr2 = np.array([a])

result = arr * arr2
print(result)

print("Конец 1 задания!")

# Задание 2
# Создайте матрицу размерностью 12 x 12, транспонируйте её, возведите каждый элемент матрицы в квадрат и умножьте на 2.
# Вычтите из данной матрицы единичную матрицу и распечатайте результат на консоль.

print("Начало 2 задания!")
a = list(range(1, 13))

arr = np.array([a, a])
print("Транспортировка матрицы")
arr2 = arr.transpose()
print(arr2)

print("Возведение в квадрат и умножение:")
mul_arr = (arr2 ** 2) * 2
print(mul_arr)

print("Вычитание единичной матрицы")
print(mul_arr[1])

print("Конец 2 задания!")

# Задание 3
# Сгенерируйте 100 элементов от 1 до 20 используя средства Numpy

print("Начало 3 задания!")
arr = np.linspace(1, 20, 100)
print(len(arr))
print(arr)
print("Конец 3 задания!")

# Задание 4
# Сгенерируйте массив значений от 1 до 300 используя средства Numpy.
# Измените размерность данного массива на 3 x 100, а затем создайте новый массив с теми же значениями,
# но размерностью 6 x 50.

print("Начало 4 задания!")
print("От 1 до 300")
arr = np.arange(1, 301)
print(arr)
print("3 x 100")
arr2 = arr.reshape(3, 100)
print(arr2)
print("6 x 50")
arr3 = np.arange(1, 301).reshape(6, 50)
print(arr3)

print("Конец 4 задания!")