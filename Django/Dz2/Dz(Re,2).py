# Написать пример регулярного выражения, которое совпадает сразу с тремя строками: "dog", "box", "bog".
import re

text = 'dog box bog rog sox cot cox dogxsa sdad12box'

print(re.findall(r"[db]o[gx]", text))


# Написать пример регулярного выражения, которое не совпадает сразу с тремя строками:
# "dog", "box", "bog", но совпадет с “cot”

text = 'dog box bog rog sox cot cox dogxsa sdacotd12box'

print(re.findall(r"\bcot\b", text))