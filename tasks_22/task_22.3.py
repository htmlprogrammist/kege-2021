"""
Задание 22 (№277).
Получив на вход число x, эта программа печатает два числа, a и b.
Укажите наименьшее натуральное число,
при вводе которого эта программа напечатает сначала 2, потом – 9.
"""
print('Ответы по смыслу:', [605, 607, 609, 615, 617, 619, 794, 844, 858, 868])
print('Ответ по заданию:', 605)
x = int(input())
a = 0
b = 1
while x > 0:
    if x % 2 > 0:
        a += 1
    else:
        b += x % 5
    x = x // 5
print(a, b)

answer_a = 2
answer_b = 9
answers = []
x = 0

while x < 1000:
    number = x
    a = 0
    b = 1
    while number > 0:
        if number % 2 > 0:
            a += 1
        else:
            b += number % 5
        number = number // 5
    if a == answer_a and b == answer_b:
        answers.append(x)
    x += 1

print(answers)
print(min(answers))
