"""
Рассматривается множество целых чисел, принадлежащих числовому отрезку [3712; 8432],
которые удовлетворяют следующим условиям:
− запись в двоичной и четверичной системах счисления заканчивается одинаковой цифрой;
− кратны 13, 14 или 15.
Найдите количество таких чисел и минимальное из них.
"""

for i in range(8432, 3712 + 1, -1):
    current_binary_number_i = i
    current_quaternary_number_i = i
    binary_number_i = ''
    quaternary_number_i = ''
    while current_binary_number_i > 0:
        binary_number_i = str(current_binary_number_i % 2) + binary_number_i
        current_binary_number_i //= 2
    while current_quaternary_number_i > 0:
        quaternary_number_i = str(current_quaternary_number_i % 4) + quaternary_number_i
        current_quaternary_number_i //= 4
    print(i, '2', binary_number_i, '4', quaternary_number_i)
