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

dividers = []  # Простые делители
dividers_all = []  # Все делители числа, из них потом циклом с j достанем простые делители и отправим в dividers
counter_all = 0  # Счётчик всех делителей
counter_simple = 0  # Счётчик простых делителей
counter_wrong = 0  # Этот счётчик должен быть равен 0, если нет, то у нас не простой делитель
for i in range(25317, 51237 + 1):
    dividers = []
    dividers_all = []
    counter_all = 0
    # Получение всех делителей
    for k in range(2, int(math.sqrt(i)) + 1):
        if i % k == 0:
            dividers_all.append(k)
            dividers_all.append(i // k)
    # Изначально была какая-то тактика/идея.
    # Сейчас тут просто счётчик делителей // len(dividers_all)
    # for j in range(1, len(dividers_all) // 2 + 1):
    #     # if counter_all > 0:  # Этот блок игнорируется
    #     #     break
    #     for r in range(len(dividers_all)):
    #         if dividers_all[r] % j == 0:
    #             counter_all += 1
        # if dividers_all[j] % j == 0:
        #     counter_all += 1
    # Прохожусь по ВСЕМ делителям, пытаюсь найти 6 простых делителей
    # СПОЙЛЕР: делает копию списка со ВСЕМИ делителями, там даже Тру есть
    for m in range(len(dividers_all)):
        counter_wrong = 0
        for n in range(1, len(dividers_all)):
            if dividers_all[m] % n == 0:
                counter_wrong += 1
        if counter_wrong == 0:
            dividers.append(dividers_all[m])
    # if dividers == dividers_all:
    #     print(True)  # Всё True))))))))))))
    # print(dividers_all, 'Счётчик делителей =', counter_all)
    # if counter_all == 0:
    #     pass
        # print(dividers_all)  # []
    #     dividers.append(j)
    # if len(dividers) > 6:
    #     print(dividers)

# from math import sqrt
#
# a = []
# counter = 0
# counter_of_simple_numbers = 0
#
# for i in range(25317, 51237 + 1):
#     a = []
#     counter = 0
#     # for d in range(3, i + 1):
#     #     if i % j == 0:
#     #         counter_of_simple_numbers += 1
#     d = 3
#     k = 3
#     while d % k != 0:
#
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
#
#     #     for divider in range(1, j + 1):
#     #         if j % divider == 0:
#     #             counter_all += 1
#     # if counter_all == 2:
#     #     dividers.append(j)
#     # if dividers != [] and len(dividers) >= 6:
#     #     print(i, max(dividers))
