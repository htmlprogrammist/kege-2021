"""
Ниже на пяти языках программирования записана программа,
которая вводит натуральное число  выполняет преобразования,
а затем выводит одно число.
Укажите наименьшее возможное значение x,
при вводе которого программа выведет число 18
"""

x = int(input())
a = 0
b = 10
while x > 0:
    d = x % 9
    if d > a:
        a = d
    if d < b:
        b = d
    x = x // 9
print(a * b)

print('---')

answer = 0
answers = []
answer_t = 18
while answer < 100:
    x = answer
    a = 0
    b = 10
    while x > 0:
        d = x % 9
        if d > a:
            a = d
        if d < b:
            b = d
        x = x // 9
    if answer_t == a * b:
        answers.append(answer)
    answer += 1

print(answers)
print(min(answers))
