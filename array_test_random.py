from random import randint

A = []
summa = 0
counter = 0
n = 10

for i in range(n):
    A.append(randint(-100, 100))

for i in range(n - 1):
    if A[i] > A[i + 1]:
        A[i], A[i + 1] = A[i + 1], A[i]

print('Список А', A)
