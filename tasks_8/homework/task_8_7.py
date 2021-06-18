"""
100) Вася составляет 6-буквенные коды из букв П, А, Н, Е, Л, Ь. Каждую букву нужно использовать ровно 1 раз,
при этом код не может начинаться с буквы Ь и не может содержать сочетания ЕАП.
Сколько различных кодов может составить Вася?

582
"""
from itertools import product

counter = 0
p = product('ПАНЕЛЬ', repeat=6)
s = map(lambda x: "".join(x), p)

for i in s:
    if i.count('П') == 1 and i.count('А') == 1 and i.count('Н') == 1 and i.count('Е') == 1 and i.count('Л') == 1 and i.count('Ь') == 1:
        if i[0] != 'Ь' and i.count('ЕАП') == 0:
            counter += 1

print(counter)  # 582
