"""
Задание 22 (№784).
Получив на вход число d, этот алгоритм печатает число c.
Сколько положительных значений d существует таких,
что в результате выполнения программы на экран будет выведено число меньше 15?
Примечание: abs, iabs – функции, находящие абсолютное значение
"""


def F(x):
    return abs(x - 4) + abs(x + 6) - 3


d = int(input())
a = -20
b = 20
c = 1
for t in range(a, b + 1):
    if F(t) < d:
        c += 1
print(c)


# d = 1
# answers = []
# answer = 15
# while d < 500:
#     a = -20
#     b = 20
#     c = 1
#     for t in range(a, b + 1):
#         if F(t) < d:
#             c += 1
#     if c < answer:
#         answers.append(d)
#     d += 1
#
# print(answers)
# print(len(answers))
