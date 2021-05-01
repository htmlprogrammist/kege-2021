"""
Задание 22 (№585).
Ниже на четырех языках программирования записан алгоритм.
Получив на вход натуральное десятичное число x, этот алгоритм печатает число S.
Укажите наименьшее число x, большее 50,
при вводе которого на экран будет выведено число 1.
"""
# x = int(input())
# S = 0
# while x > 0:
#     if x % 2 > 0:
#         S = S + (x % 7)
#     else:
#         S = S - (x % 7)
#     x = x // 7
# print(S)

x = 50
answer = 1
answers = []

while x < 200:
    number = x
    S = 0
    while number > 0:
        if number % 2 > 0:
            S = S + (number % 7)
        else:
            S = S - (number % 7)
        number = number // 7
    if S == answer:
        answers.append(x)
    x += 1

print(answers)
print(min(answers))

