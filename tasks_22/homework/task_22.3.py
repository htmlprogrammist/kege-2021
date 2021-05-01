"""
Задание 22 (№728).
Получив на вход число x, этот алгоритм печатает число M. Известно, что x > 100.
Укажите наименьшее такое (т. е. большее 100) число x,
при вводе которого алгоритм печатает 9.
"""
# x = int(input())
# L = x - 18
# M = x + 36
# while L != M:
#     if L > M:
#         L = L - M
#     else:
#         M = M - L
# print(M)

x = 100
answer = 9
answers = []

while x < 1000:
    number = x
    L = number - 18
    M = number + 36
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == answer:
        answers.append(x)
    x += 1

print(answers)
print(min(answers))
