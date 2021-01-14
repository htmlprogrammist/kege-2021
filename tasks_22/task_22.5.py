"""
Задание 22 (№632).
Ниже приведён алгоритм.
Получив на вход число x, этот алгоритм печатает число S.
Укажите наибольшее число x, при вводе которого алгоритм печатает 82.
"""

# x = int(input())
# P = 90
# S = 6 * (x - x % 22)
# K = 0
# while P < 181:
#     K = K + 1
#     P = P + K
#     S = S - 2 * K
# print(S)  # 82


answer = 82
answers = []
x = 0
while x < 500:
    number = x
    P = 90
    S = 6 * (number - number % 22)
    K = 0
    while P < 181:
        K = K + 1
        P = P + K
        S = S - 2 * K
    if S == answer:
        answers.append(x)
    x += 1

print(answers)
print(max(answers))
