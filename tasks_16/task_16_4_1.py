"""
№ 724, Джобс 23.11.2020
Алгоритм вычисления функций F(n) и G(n) задан следующими соотношениями:
F(n) = G(n) = 1 при n = 1
F(n) = F(n–1) – 2 · G(n–1), при n > 1
G(n) = F(n–1) + G(n–1) + n, при n > 1
Чему равна сумма цифр значения функции G(36)?

40
"""
F = [1] * 37
G = [1] * 37
F[1] = G[1] = 1
for i in range(2, 36 + 1):
    F[i] = F[i - 1] - 2 * G[i - 1]
    G[i] = F[i - 1] + G[i - 1] + i


summa = 0
string = G[36]
for number in str(string):
    summa += int(number)

print(summa)
