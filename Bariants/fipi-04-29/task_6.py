"""
Задание 6 (№1286).
Определите, при каком наибольшем введённом значении переменной s программа выведет число 64.
Для Вашего удобства программа представлена на четырёх языках программирования.
"""
s = int(input())
n = 1
while s < 47:
    s += 4
    n *= 2
print(n)

number = 1
while number < 1000:
    s = number
    n = 1
    while s < 47:
        s += 4
        n *= 2
    if n == 64:
        mx = number
    number += 1
print(mx)  # 26