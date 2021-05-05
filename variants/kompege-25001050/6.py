"""
Задание 6 (№871).
Определите,
при каком наименьшем положительном введённом значении переменной s
программа выведет число s, отличающееся от введенного значения.
"""
s = int(input())
n = 100
while s - n >= 100:
    s += 20
    n += 40
print(s)

number = 1
while number < 1000:
    s = number
    n = 100
    while s - n >= 100:
        s += 20
        n += 40
    if s != number:
        print(number)
        break
    number += 1
