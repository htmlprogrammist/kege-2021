"""
Укажите наименьшее число x,
при вводе которого алгоритм печатает сначала 6, а потом 7
"""

x = int(input())
L = 0
M = 0
while x > 0:
    M = M + 1
    if x % 2 == 0:
        L = L + 1
    x = x // 2
print(L)
print(M)

print('---')

answer = 0
answers = []
answer_L = 6
answer_M = 7
while answer < 200:
    x = answer
    L = 0
    M = 0
    while x > 0:
        M = M + 1
        if x % 2 == 0:
            L = L + 1
        x = x // 2
    if answer_L == L and answer_M == M:
        answers.append(answer)
    answer += 1

print(answers)
print(min(answers))
