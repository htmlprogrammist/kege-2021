"""
№ 91, Джобс 07.09.2020
Иннокентий составляет семибуквенные слова из букв Е, И, Й, К, Н, О, Т.
Сколько слов может составить Иннокентий, если известно, что в каждом из них есть комбинация КОТ?
"""
from itertools import product

counter = 0


def isKot(s):
    flag = False
    for k in range(len(s)-2):
        if s[k] == 'К' and s[k + 1] == 'О' and s[k + 2] == 'Т':
            flag = True
    return flag


for i in product('ЕИЙКНОТ', repeat=7):
    if isKot(i):
        counter += 1

print(counter)  # 11984
