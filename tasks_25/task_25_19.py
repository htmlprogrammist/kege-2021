"""
Задание 25 (№935).
Выведите 6 чисел по порядку, начиная с 700000, таких, что количество натуральных делителей каждого следующего числа
будет превосходить количество натуральных делителей предыдущего выведенного числа.
В качестве ответа приведите 6 пар – найденное число и количество его натуральных делителей.

700000 72
700128 144
702000 160
702240 192
720720 240
1081080 256
"""
counter_o = 0
numbers = []
amount_of_delitels = []
prev = 0

for i in range(700000, 11000000):
    counter_d = 2  # включаю 1 и само число
    if (i ** 0.5) == int(i ** 0.5):
        counter_d += 1
    for j in range(2, int(i ** 0.5)):
        if i % j == 0:
            counter_d += 2
    if counter_d > prev:
        counter_o += 1
        numbers.append(i)
        amount_of_delitels.append(counter_d)
        prev = counter_d
    if counter_o == 6:
        break

for i in range(len(numbers)):
    print(numbers[i], amount_of_delitels[i])
