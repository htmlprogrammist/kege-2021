"""
(№ 1796) (А.Г. Минак)
Определите, при каком наименьшем положительном введённом значении переменной s программа выведет четырехзначное число.

343
"""
s = int(input())
n = 127
while s - n > 0:
    s = s + 15
    n = n + 20
print(s)

number = 0
while number < 1000:
    s = number
    n = 127
    while s - n > 0:
        s = s + 15
        n = n + 20
    if len(str(s)) == 4:
        print(number)
        break
    number += 1
