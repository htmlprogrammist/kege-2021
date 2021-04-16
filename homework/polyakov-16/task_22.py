"""
(№ 420) Ниже записан алгоритм. Получив на вход число x, этот алгоритм печатает число M.
Известно, что x > 100. Укажите наименьшее такое (т.е. большее 100) число x, при вводе которого алгоритм печатает 35.

120
"""
x = int(input())
L = x - 15
M = x + 20
while L != M:
    if L > M:
        L = L - M
    else:
        M = M - L
print(M)

number = 100
while number < 1000:
    x = number
    L = x - 15
    M = x + 20
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 35:
        print(number)
        break
    number += 1
