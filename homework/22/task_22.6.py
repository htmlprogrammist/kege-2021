""" Ya.Tutor
Ниже на пяти языках программирования записана программа,
которая вводит натуральное число  выполняет преобразования,
а затем выводит два числа.
Укажите наименьшее возможное значение  при вводе которого программа выведет
сначала 3, а потом 2
"""

x = int(input())
a = 0
b = 0
while x > 0:
    if x % 2 == 0:
        a += 1
    else:
        b += 1
    x = x // 2
print(a, b)

answer = 0
answers = []
answer_a = 3
answer_b = 2
while answer < 100:
    x = answer
    a = 0
    b = 0
    while x > 0:
        if x % 2 == 0:
            a += 1
        else:
            b += 1
        x = x // 2
    if answer_a == a and answer_b == b:
        answers.append(answer)
    answer += 1

print(answers)
print(min(answers))
