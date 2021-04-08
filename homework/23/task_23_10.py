"""
№ 1063, Джобс 15.03.2021
Исполнитель преобразует число, записанное на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
3. Сделать нечетное
Первая команда увеличивает число на 1, вторая – вдвое, третья прибавляет к четному числу 1, к нечетному – 2.
Программа для исполнителя – это последовательность команд. Сколько существует таких программ,
которые исходное число 3 преобразуют в число 25 и при этом траектория вычислений программы содержит число 9 и число 17?

229635
"""
k = [0] * (25 + 1)
k[3] = 1

for n in range(3, 9 + 1):
    if n + 1 <= 9:
        k[n + 1] += k[n]
    if n * 2 <= 9:
        k[n * 2] += k[n]
    if n % 2 == 0 and n + 1 <= 9:
        k[n + 1] += k[n]
    if n % 2 != 0 and n + 2 <= 9:
        k[n + 2] += k[n]

for n in range(9, 17 + 1):
    if n + 1 <= 17:
        k[n + 1] += k[n]
    if n * 2 <= 17:
        k[n * 2] += k[n]
    if n % 2 == 0 and n + 1 <= 17:
        k[n + 1] += k[n]
    if n % 2 != 0 and n + 2 <= 17:
        k[n + 2] += k[n]

for n in range(17, 25 + 1):
    if n + 1 <= 25:
        k[n + 1] += k[n]
    if n * 2 <= 25:
        k[n * 2] += k[n]
    if n % 2 == 0 and n + 1 <= 25:
        k[n + 1] += k[n]
    if n % 2 != 0 and n + 2 <= 25:
        k[n + 2] += k[n]

print(k[25])
