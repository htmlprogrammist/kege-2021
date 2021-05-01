"""
Задание 25 (№680).
Рассматриваются целые числа, принадлежащих числовому отрезку [485617; 529678],
которые представляют собой произведение трёх различных простых делителей,
оканчивающихся на одну и ту же цифру. В качестве ответа приведите все числа,
разность максимального и минимального простых делителей которого меньше 100.
Для каждого такого числа сначала запишите само число,
а затем разность максимального и минимального простых делителей

487813 60
497087 60
500477 70
502793 90
508049 50
"""
import math
simple_counter = 0
dividers = []
k, j = 0, 0

for i in range(485617, 529678 + 1):
    simple_counter = 0
    dividers = []
    for d in range(2, int(math.sqrt(i)) + 1):
        if i % d == 0:
            k = 0
            for j in range(2, int(math.sqrt(d)) + 1):
                if d % j == 0:
                    k += 1
            if k == 0:
                simple_counter += 1
                dividers.append(d)
    if simple_counter == 3:
        # if i == 487813:
        #     print('487813', dividers)  # 487813 [47, 97, 107]
        # if i == 497087:
        #     print('497087', dividers)  # 497087 [53, 83, 113]
        # if i == 500477:
        #     print('500477', dividers)  # 500477 [43, 103, 113]
        # if i == 502793:
        #     print('502793', dividers)  # 502793 [37, 107, 127]
        # if i == 508049:
        #     print('508049', dividers)  # 508049 [59, 79, 109]
        if dividers[0] * dividers[1] * dividers[2] == i:
            difference = dividers[2] - dividers[0]
            if difference < 100:
                if dividers[0] % 10 == dividers[1] % 10 == dividers[2] % 10:
                    print(i, difference)
