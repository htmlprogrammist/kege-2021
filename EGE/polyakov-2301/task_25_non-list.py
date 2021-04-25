"""
Задание 25 (К. Амеличев)
Среди целых чисел, принадлежащих числовому отрезку [4099; 26985], найдите числа,
имеющие ровно один натуральный делитель, не считая единицы и самого числа.
В ответе запишите два числа: сначала количество найденных чисел, а затем сумму цифр этих чисел.
"""
total = 0
counter = 0

for i in range(4099, 26985 + 1):
    delitel = 0

    if (i ** 0.5).is_integer():
        delitel += 1

    for j in range(2, round(i ** 0.5)):
        if i % j == 0:
            delitel += 2

    if delitel == 1:
        number = i
        while number > 0:
            total += number % 10
            number //= 10
        counter += 1

print(counter, total)
