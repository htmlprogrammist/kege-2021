"""
№ 724, Джобс 23.11.2020
Алгоритм вычисления функций F(n) и G(n) задан следующими соотношениями:
F(n) = G(n) = 1 при n = 1
F(n) = F(n–1) – 2 · G(n–1), при n > 1
G(n) = F(n–1) + G(n–1) + n, при n > 1
Чему равна сумма цифр значения функции G(36)?

40
"""
from functools import *


@lru_cache()
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) - 2 * G(n - 1)


def G(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) + G(n - 1) + n


string = str(G(36))
summa = 0

for number in string:
    summa += int(number)

print(summa)
