"""
Задание 25 (№680).
Рассматриваются целые числа, принадлежащих числовому отрезку [485617; 529678],
которые представляют собой произведение трёх различных простых делителей,
оканчивающихся на одну и ту же цифру. В качестве ответа приведите все числа,
разность максимального и минимального простых делителей которого меньше 100.
Для каждого такого числа сначала запишите само число,
а затем разность максимального и минимального простых делителей


"""
import math

dividers = []
k, j = 0, 0

for i in range(485617, 529678 + 1):
    dividers = []
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            k = 0
            for d in range(2, int(math.sqrt(i)) + 1):
                if j % d == 0:
                    k += 1
            if k == 0:
                dividers.append(j)

    if dividers:
        print(dividers)