"""
№ 633, Джобс 02.11.2020
У исполнителя Калькулятор три команды, которым присвоены номера:
1. прибавь 1
2. умножь на 2
3. возведи в квадрат
Сколько есть программ, которые число 5 преобразуют в число 154?

8966
"""
k = [0] * (154 + 1)
k[5] = 1
for n in range(5, 154 + 1):
    if (n + 1) <= 154:
        k[n + 1] += k[n]
    if (n * 2) <= 154:
        k[n * 2] += k[n]
    if (n ** 2) <= 154:
        k[n ** 2] += k[n]
print(k[154])
