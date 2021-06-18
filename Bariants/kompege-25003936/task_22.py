"""
Задание 22 (№1427). Получив на вход натуральное число x, этот алгоритм печатает два числа.
Сколько существует натуральных чисел, при вводе которых алгоритм печатает сначала 16, а затем 14.
"""
x = int(input())
a = 0
b = 0
while x > 0:
    a += 1
    if x % 2 != 0:
        b += 1
    x //= 2
print(a, b)

counter = 0
number = 1
while number < 100000:
    x = number
    a = 0
    b = 0
    while x > 0:
        a += 1
        if x % 2 != 0:
            b += 1
        x //= 2
    if a == 16 and b == 14:
        counter += 1
    number += 1
print(counter)
