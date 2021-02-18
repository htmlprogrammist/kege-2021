"""
Алгоритм вычисления значения функции F(n), где n – целое неотрицательное
число, задан следующими соотношениями:
F(0) = 0;
F(n) = F(n/2), если n > 0 и при этом n чётно;
F(n) = 1 + F(n – 1), если n нечётно.
Назовите минимальное значение n, для которого F(n) = 12.
"""


def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n/2)
    if n % 2 != 0:
        return 1 + F(n-1)


for n in range(4096):
    a = F(n)
    if a == 12:
        print(n)
        break
