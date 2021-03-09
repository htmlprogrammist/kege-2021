"""
№ 805, Джобс 07.12.2020
Алгоритм вычисления функций F(n)? Где n – натуральное число, задан следующими соотношениями:
F(n) = n – 1 при n < 4,
F(n) = n + 2*F(n – 1), когда n > 3 и кратно 3
F(n) = F(n – 2) + F(n – 3), когда n > 3 и не кратно 3.
Чему равна сумма цифр значения функции F(25)?

13
"""
F = [1] * (25 + 1)

for n in range(1, 4):
    F[n] = n - 1

for n in range(4, 25 + 1):
    if n > 3 and n % 3 == 0:
        F[n] = n + 2 * F[n - 1]
    if n > 3 and n % 3 != 0:
        F[n] = F[n - 2] + F[n - 3]

string_number = F[25]
summa = 0
for n in str(string_number):
    summa += int(n)

print(summa)
