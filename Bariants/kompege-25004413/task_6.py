"""
Задание 6 (№871).
Определите, при каком наименьшем положительном введённом значении переменной s программа выведет число s,
отличающееся от введенного значения.
"""
s = int(input('Enter: '))
n = 100
while s - n >= 100:
    s += 20
    n += 40
print('S:', s)

for number in range(1, 1000):
    s = number
    n = 100
    while s - n >= 100:
        s += 20
        n += 40
    if s != number:
        print('Answer:', number)
        break
