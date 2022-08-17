# def find_missing(sequence):
#     num = sequence[1] - sequence[0]
#     if not sequence[3] - sequence[2] == num:
#         num = sequence[-1] - sequence[-2]
#
#     for i in range(len(sequence)):
#         if not sequence[i] + num == sequence[i+1]:
#             result = sequence[i] + num
#             break
#     return result
#
#
# print(find_missing([1, -2, -5, -8, -14, -17, -20, -23, -26]))
# print(find_missing([-13, 5, 14, 23, 32, 41, 50, 59, 68]))
# print(find_missing([-1, -7, -10, -13, -16, -19, -22, -25, -28]))

# def find_missing(sequence):
#     num = sequence[1] - sequence[0]
#     if sequence[3] - sequence[2] == num:
#         pass
#     else:
#         num = sequence[-1] - sequence[-2]
#
#     for i in range(len(sequence)):
#         if sequence[i] + num == sequence[i+1]:
#             pass
#         else:
#             result = sequence[i] + num
#             break
#     return result


def fibbo(n):
    def cache_fibbo(n, m):
        if n in m:
            return m[n]

        answer = cache_fibbo(n-1, m) + cache_fibbo(n-2, m)

        m[n] = answer
        return answer
    m = {0: 0, 1: 1}
    return cache_fibbo(n, m)
