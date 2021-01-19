"""
Укажите наименьшее возможное значение x,
при вводе которого программа выведет число 12
"""

x = int(input())
a = 0
b = 10
while x > 0:
    d = x % 6
    if d > a: a = d
    if d < b: b = d
    x = x // 6
print(a * b)

print('---')

answer = 0
answers = []
answer_t = 12
while answer < 200:
    x = answer
    a = 0
    b = 10
    while x > 0:
        d = x % 6
        if d > a: a = d
        if d < b: b = d
        x = x // 6
    if answer_t == a * b:
        answers.append(answer)
    answer += 1

print(answers)
print(min(answers))
