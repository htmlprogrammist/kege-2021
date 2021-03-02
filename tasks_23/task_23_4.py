"""
№ 633, Джобс 02.11.2020
У исполнителя Калькулятор три команды, которым присвоены номера:
1. прибавь 1
2. умножь на 2
3. возведи в квадрат
Сколько есть программ, которые число 5 преобразуют в число 154?

8966
"""
import math
k = [1] * (154 + 1)

for n in range(5, 154 + 1):
    k[n] = k[n - 1]

    if n > 9 and n % 2 == 0:
        k[n] += k[n // 2]

    if n > 24 and math.sqrt(n).is_integer():
        k[n] += k[int(math.sqrt(n))]

print(k[154])