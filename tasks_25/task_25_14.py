"""
Найдите все натуральные числа, принадлежащие отрезку [45 000 000;50 000 000],
у которых ровно пять различных нечётных делителей
(количество чётных делителей может быть любым).
В ответе перечислите найденные числа в порядке возрастания
(в отдельные поля для ответов).
"""
from math import sqrt
for i in range(45000000, 50000000 + 1):
    counter_odd_del = 1
    if int(sqrt(i))**2 == i and int(sqrt(i)) % 2 != 0:
        counter_odd_del += 1
    if i % 2 != 0:
        counter_odd_del += 1
    for j in range(2, int(sqrt(i))):
        if i % j == 0:
            if j % 2 != 0:
                counter_odd_del += 1
            if (i//j) % 2 != 0:
                counter_odd_del += 1
        if counter_odd_del > 5:
            break
    if counter_odd_del == 5:
        print(i)
