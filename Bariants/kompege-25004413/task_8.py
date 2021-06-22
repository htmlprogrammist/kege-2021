"""
Задание 8 (№197). Вася составляет 5-буквенные коды из букв К, А, Л, И, Й. Каждую букву нужно использовать ровно 1 раз,
при этом код не может начинаться с буквы Й и не может содержать сочетания ИА.
Сколько различных кодов может составить Вася?

78
"""
from itertools import product

p = product('КАЛИЙ', repeat=5)
s = map(lambda x: "".join(x), p)
k = 0
# s = ['КАЛИЙ', 'ККАИК', 'ККИАК', 'КИАЛЙ', 'КЛЙИА']


def f(x):
    flag = True
    for j in range(len(x) - 1):
        if x[j:j+2] == 'ИА':
            flag = False
    return flag


for i in s:
    if len(set(i)) == 5:
        if i[0] != "Й" and f(i):
            k += 1

print(k)
