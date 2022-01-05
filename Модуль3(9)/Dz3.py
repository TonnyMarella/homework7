import pickle
import json

lst = ["Монитор", "Клавиатура", "Компьютерная мышь", "Колонки", "Ноутбук"]

with open('test2.txt', 'wb') as f:
    pickle.dump(lst, f)

with open('test2.txt', 'rb') as f:
    T2 = pickle.load(f)
    print('PICKLE = ', T2)

with open('test2.txt', 'w') as f:
    json.dump(lst, f)

with open('test2.txt', 'r') as f:
     T3 = json.load(f)
     print('JSON =', T3)
