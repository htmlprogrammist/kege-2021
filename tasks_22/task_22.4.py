"""
Задание 22 (№677).
Укажите минимальное натуральное число,
при вводе которого этот алгоритм напечатает число, сумма цифр которого равна 15.
"""

x = int(input())
L = 0
M = 1
while x > 0:
    L = x % 10 * M + L
    x = x // 10
    M = M * 10
print(L)  # Сумма цифр L будет 15

sum_of_L = 0
answer_sum_of_L = 15
number = 0
answers = []
while number < 500:
    x = number
    sum_of_L = 0
    L = 0
    M = 1
    while x > 0:
        L = x % 10 * M + L
        x = x // 10
        M = M * 10
    number_L = L
    while number_L > 0:
        sum_of_L += number_L % 10
        number_L //= 10
    if sum_of_L == answer_sum_of_L:
        answers.append(number)
    number += 1

print(answers)
print(min(answers))
