"""
Задание 6 (№527).
Найдите минимальное значение d, при котором в результате работы программы на экране будет напечатано число 67.
Для Вашего удобства программа представлена на четырех языках программирования.
"""
d = int(input())
n = 2
s = 0
while s <= 365:
    s += d
    n += 5
print(n)

for i in range(1, 1000):
    d = i
    n = 2
    s = 0
    while s <= 365:
        s += d
        n += 5
    if n == 67:
        print(i)
        break