"""
№ 628, Джобс 02.11.2020
Алгоритм вычисления функции F(n) задан следующими соотношениями:
F(n) = n + 3, при n ≤ 18
F(n) = (n // 3) · F(n // 3) + n – 12, при n > 18, кратных 3
F(n) = F(n–1) + n · n + 5, при n > 18, не кратных 3
Здесь «//» обозначает деление нацело.
Определите количество натуральных значений n из отрезка [1; 1000],
для которых все цифры значения F(n) чётные.

16
"""
counter = 0


def F(n):
    if n <= 18:
        return n + 3
    if n > 18 and n % 3 == 0:
        return (n // 3) * F(n // 3) + n - 12
    if n > 18 and n % 3 != 0:
        return F(n-1) + n * n + 5


for n in range(1, 1000 + 1):
    even = True
    result = F(n)
    for number in str(result):
        if int(number) % 2 != 0:
            even = False
    if even:
        counter += 1

print(counter)
