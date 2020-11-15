"""
Задание 25 (№506).
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [25317; 51237],
которые имеют хотя бы 6 различных простых делителей. Делители 1 и само число не учитываются.
В качестве результата работы программы приведите
найденное число и максимальный простой делитель этого числа.

30030 13
39270 17
43890 19
46410 17
"""
import math

dividers = []
dividers_all = []
counter = 0
simple_counter = 0
for i in range(25317, 51237 + 1):
    dividers = []
    simple_counter = 0
    dividers_all = []
    for k in range(2, int(math.sqrt(i)) + 1):
        if i % k == 0:
            dividers_all.append(k)
            dividers_all.append(i // k)
    for j in range(1, dividers_all):
        if dividers_all[j] % j == 0:
            simple_counter += 1
    if simple_counter == 0:
        # for j in range(1, len(dividers_all)):
        #     if simple_counter > 0:
        #         break
        #     if dividers_all[j] % j == 0:
        #         simple_counter += 1
        # if simple_counter == 0:
        #     dividers.append(j)
        # if len(dividers) > 6:
        #     print(dividers)

        # """
        # Задание 25 (№506).
        # Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [25317; 51237],
        # которые имеют хотя бы 6 различных простых делителей. Делители 1 и само число не учитываются.
        # В качестве результата работы программы приведите
        # найденное число и максимальный простой делитель этого числа.

        # 30030 13
        # 39270 17
        # 43890 19
        # 46410 17
        # """
        # from math import sqrt

        # a = []
        # counter = 0
        # counter_of_simple_numbers = 0

        # for i in range(25317, 51237 + 1):
        #     a = []
        #     counter = 0
        #     # for d in range(3, i + 1):
        #     #     if i % j == 0:
        #     #         counter_of_simple_numbers += 1
        #     d = 3
        #     k = 3
        #     while d % k != 0:

        #         # if counter_of_simple_numbers == 2:
        #         #     a.append(j)
        #         #     a.append(j)
        #         #     counter += 1
        #         # if counter >= 6:
        #         #     for k in range(len(a)):
        #         #         # print(k, a[k])
        #         #         # print(a.index(k))
        #         #         ranger = a[k]
        #         #         for m in range(1, ranger + 1):
        #         #             if ranger % m == 0:
        #         #                 counter_of_simple_numbers += 1
        #         # if counter_of_simple_numbers == 2:
        #         #     print(i, ranger)

        #     #     for divider in range(1, j + 1):
        #     #         if j % divider == 0:
        #     #             simple_counter += 1
        #     # if simple_counter == 2:
        #     #     dividers.append(j)
        #     # if dividers != [] and len(dividers) >= 6:
        #     #     print(i, max(dividers))
