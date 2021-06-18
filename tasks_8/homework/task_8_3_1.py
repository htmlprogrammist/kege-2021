"""
Вася составляет 4-буквенные коды из букв У, Л, Е, Й. Каждую букву нужно использовать ровно 1 раз,
при этом код не может начинаться с буквы Й и не может содержать сочетания ЕУ.
Сколько различных кодов может составить Вася?
"""
from itertools import product

p = product('УЛЕЙ', repeat=4)
s = map(lambda x: "".join(x), p)
counter = 0

for i in s:
    if i[0] != 'Й' and i.count('ЕУ') == 0 and i.count('У') and i.count('Л') == 1 and i.count('Е') == 1 and i.count('Й') == 1:
        counter += 1
print(counter)
