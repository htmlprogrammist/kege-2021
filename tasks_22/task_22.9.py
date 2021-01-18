"""
Задание 22 (№437).
Ниже на четырех языках программирования записан алгоритм.
Получив на вход натуральное десятичное число x, этот алгоритм печатает число S.
Известно, что в результате работы программы на экран выведено
минимально возможное число большее 25.
Укажите минимальное число x для которого это возможно.
"""

x = int(input())
S = 1
A = 11
while x // 7 > 0:
    if x % 7 < 4:
        S += A
    else:
        S += x % 7
    x //= 7
print(S)
print('---')

x = 0
answers = []
answer_S = 26
# minimal_S = 25
while x < 3000:
    number = x
    S = 1
    A = 11
    while number // 7 > 0:
        if number % 7 < 4:
            S += A
        else:
            S += number % 7
        number //= 7
    if S == answer_S:
        answers.append(x)
    x += 1
print(answers)
print(min(answers))
