"""
Задание 22 (№503).
Ниже на четырех языках программирования записан алгоритм.
Получив на вход натуральное десятичное число x, этот алгоритм печатает число S.
Сколько существует чисел x, не превышающих 500,
при вводе которых результате работы программы на экране будет выведено число 13.
"""

# x = int(input())
# S = 0
# while x > 0:
#     if x % 5 > 0:
#         S = S + (x % 5)
#     else:
#         S = S * (x % 5)
#     x = x // 5
# print(S)


# def task(x):
#     while x > 0:
#         if x % 5 > 0:
#             S = S + (x % 5)
#         else:
#             S = S * (x % 5)
#         x = x // 5
#     return S


answer = 13
x = 0
a = []
while x <= 500:
    number = x
    S = 0
    # task(number)
    while number > 0:
        if number % 5 > 0:
            S = S + (number % 5)
        else:
            S = S * (number % 5)
        number = number // 5
    if S == answer:
        a.append(x)
    x += 1
print(len(a))
