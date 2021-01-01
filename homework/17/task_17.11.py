"""
Рассматривается множество целых чисел, принадлежащих числовому отрезку [1476; 7039],
которые удовлетворяют следующим условиям:
− кратны 2, но не кратны 16;
− цифра в разряде десятков не менее 4.
Найдите количество таких чисел и
среднее арифметическое минимального и максимального из них.
Обратите внимание на то, что второе число не должно содержать десятичной запятой.

1455 4237
"""
counter = 0
numbers = []

for i in range(1476, 7039 + 1):
    number = i
    digits = []
    while number > 0:
        last_digit = number % 10
        digits.append(last_digit)
        number //= 10
    if i % 2 == 0 and i % 16 != 0 and digits[1] >= 4:
        counter += 1
        numbers.append(i)
print(numbers)
# print(max(numbers), min(numbers))  # 6998 1476. Разница между ними = 5522
print(counter, (max(numbers) - min(numbers)) // 2)
