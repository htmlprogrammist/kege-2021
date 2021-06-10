"""
Задание 22 (№1375).
Ниже записана программа. Получив на вход число x, эта программа печатает два числа L и M.
При каком наибольшем значении x после выполнения программы на экран будет выведено два числа 3, а затем 7.
"""
x = int(input())
L, M = 0, 0
while x > 12:
    L += 1
    x //= 4
M = x
if L > M:
    L, M = M, L
print(L)  # 3
print(M)  # 7

answer_L = 3
answer_M = 7
number = 1
while number < 1000:
    x = number
    L, M = 0, 0
    while x > 12:
        L += 1
        x //= 4
    M = x
    if L > M:
        L, M = M, L
    if answer_M == M and answer_L == L:
        print('X:', number)
    number += 1
