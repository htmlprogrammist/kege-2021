"""
**Задание 22 (№703).**

Получив на вход натуральное число x, этот алгоритм печатает два числа: a и b.
Укажите наибольшее трёхзначное натуральное число, при вводе которого алгоритм печатает сначала 1, а потом 8.
```
x = int(input())
a = 0
b = 1
while x > 0:
    if x % 2 > 0:
        a = a + (x % 11)
    else:
        b = b * (x % 11)
    x = x // 11
print(a)
print(b)
```
"""


answer_a = 1
answer_b = 8
answers = []
x = 0
while x < 1000:
    number = x
    a = 0
    b = 1
    while number > 0:
        if number % 2 > 0:
            a = a + (number % 11)
        else:
            b = b * (number % 11)
        number = number // 11
    if answer_a == a and answer_b == b:
        answers.append(x)
    x += 1

print(answers)
print(max(answers))
