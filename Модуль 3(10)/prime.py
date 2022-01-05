def even_last(numbers):
    result = 0

    for i in range(0, len(numbers), 2):
        result += numbers[i] * numbers[-1]

    return len(numbers)

print(even_last([1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -4]))
