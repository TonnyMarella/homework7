# 1.Написать пример регулярного выражения, которое совпадает сразу с тремя строками:
# "cat", "cbt", "ctt".
# 2.Написать пример регулярного выражения, которое совпадает с "c", "cat", "catat" или "catatatatat".
# 3.Написать пример регулярного выражения, которое будет совпадать “c", "cat",
# но не будет совпадать целиком с "catat" или "catatatatat", а будет совпадать только с “cat” в них.

import re

value = "catatatatat 1231 2sdf cat catat sdgf12341 сat cbt cat c csd 2sdfsd f2312 dogogog dogogog dogogog"

print(re.findall(r"\bc[abt]t\b", value))

print(re.findall(r"\bc[at]{,10}\b", value))

print(re.findall(r"\bc[at]{,3}\b", value))


