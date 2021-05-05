"""
Задание 22 (№1032).
Найдите минимальное число, при вводе которого приведенный алгоритм напечатает на экране сначала 5, затем 24.
"""
x = int(input())
p, s = 1, 0
while x > 0:
    if x % 2 == 0:
        p *= (x % 10)
    else:
        s += (x % 10)
    x //= 10
print(s)  # 5
print(p)  # 24

number = 0
m = 999999999
while number < 500:
    x = number
    p, s = 1, 0
    while x > 0:
        if x % 2 == 0:
            p *= (x % 10)
        else:
            s += (x % 10)
        x //= 10
    if s == 5 and p == 24:
        m = min(m, number)
    number += 1
print(m)
