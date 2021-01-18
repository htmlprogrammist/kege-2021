"""
Выведет 4, потом 5. Наибольший X
"""
x = int(input())
Q = 9
L = 0

while x >= Q:
    L += 1
    x -= Q
M = x
if M < L:
    M = L
    L = x
print(L)
print(M)


answer_L = 4
answer_M = 5
x = 0
answers = []
while x < 1000:
    Q = 9
    L = 0
    number = x
    while number >= Q:
        L += 1
        number -= Q
    M = number
    if M < L:
        M = L
        L = number
    if M == answer_M and L == answer_L:
        answers.append(x)
    x += 1
print(answers)
print(max(answers))
