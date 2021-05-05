"""
Определите, при каком наименьшем введённом значении переменной S
программа выведет число 13. Для Вашего удобства программа представлена
на четырёх языках программирования.
"""
s = int(input())
s = 10 * s + 7
n = 1
while s < 2021:
    s += 2 * n
    n += 1
print(n)

number = 0
answer = 13
while number < 1000:
    s = number
    s = 10 * s + 7
    n = 1
    while s < 2021:
        s += 2 * n
        n += 1
    if n == answer:
        print(number)
        break
    number += 1
