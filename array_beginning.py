n = 6
a = []
counter = 0

# for i in range(n):
#     a.append(int(input()))
# print('Hello', -20 % 3)
# for j in range(len(a)-1):
#     if (a[j] % 2 == 0 and a[j+1] % 2 != 0) or (a[j] % 2 != 0 and a[j+1] % 2 == 0):
#         counter += 1

# Сумма нечетная, тройка по убыванию
# for j in range(len(a)-2):
#     if (a[j] + a[j+1] + a[j+2]) % 2 != 0 and (a[j] > a[j+1] > a[j+2]):
#         counter += 1

# for j in range(len(a)-2):
#     if (9 < a[j] < 100) and (9 < a[j + 1] < 100) and (9 < a[j + 2] < 100):
#         counter += 1

# Найти и вывести макс среди трёхзначных элементов массива, они не должны делиться на 20,
# иначе должно быть сообщение, что такого элемента нет

# b = []
# for j in range(len(a)):
#     if 99 < a[j] < 1000 and a[j] % 20 != 0:
#         b.append(a[j])
# if b:
#     print(max(b))
#     print(len(b))
# else:
#     print('Такого элемента нет')

# Найти и вывести минимальное значение среди отрицательных элементов массива,
# оканчивающихся на 3 или вывести сообщение: "Не найдено"

# min_aj = 0
# for j in range(len(a)):
#     if abs(a[j]) % 10 == 3 and a[j] < 0:
#         if a[j] < min_aj:
#             min_aj = a[j]
#
# if min_aj == 0:
#     print('Не найдено')
# else:
#     print('Min', min_aj)

# Вывести второй максимум
# Алгоритм сортировки - метод пузырька
# for j in range(len(a) - 1):
#     for k in range(j + 1, len(a)):
#         if a[j] < a[k]:
#             a[j], a[k] = a[k], a[j]
# print(a[1])
# print(a)

# Наибольший общий делитель
#
# number1 = int(input())
# number2 = int(input())
# a = number1
# b = number2
#
#
# # Алгоритм Евклида - находим общий делитель
# while number1 != number2:
#     if number1 > number2:
#         number1 = number1 - number2
#     else:
#         number2 -= number1
# print(number1)
#
# # Наим. общее кратное
# nok = a * b // number1
# print(nok)

# Имеется набор данных, состоящих из 6 пар положительных целых чисел.
# Надо выбрать из пары по одному числу, чтобы итоговая сумма всех выбранных чисел,
# не делилась на 5 и была максимально возможной

# list1 = [[1, 5], [7, 12], [10, 13], [3, 4], [5, 5], [1, 1]]
# pass

# ДЗ 06.12.2020 в WhatsApp.