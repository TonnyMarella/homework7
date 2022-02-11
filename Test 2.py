import pandas as pd
import matplotlib.pyplot as mtl

mtl.title("График усталости за неделю")
result = pd.Series({
    "Понедельник": 40,
    "Вторник": 10,
    "Среда": 90,
    "Четверг": 80,
    "Пятница": 70,
    "Суббота": 20,
    "Воскресенье": 30,
    })
mtl.plot(result)
mtl.show()