"""
Задание 5 (№262).
Автомат обрабатывает натуральное число N < 128 по следующему алгоритму:
1) Строится восьмибитная двоичная запись числа N.
2) Инвертируются разряды исходного числа (0 заменяется на 1, 1 на 0).
3) К полученному двоичному числу прибавляют единицу.
4) Полученное число переводится в десятичную систему счисления.
Для какого числа N результат работы алгоритма равен 221?

35
"""

answers = []

for i in range(128):
    binary = bin(i)[2:]
    binary_inverted = ''

    if len(binary) < 8:
        binary = '0' * (8 - len(binary)) + binary
    # print(i, binary)

    for j in range(len(binary)):
        if binary[j] == '0':
            binary_inverted += '1'
        else:
            binary_inverted += '0'
    result = binary_inverted + '1'
    # print(binary_inverted)
    # print(result)
    # print(int(result, 2))
    if int(result, 2) == 221:
        answers.append(i)

# print(bin(221))  # 11011101
# По сути, это binary_inverted => просто binary будет равна 00100010 = 34 в десятичной, но не 35...
print(answers)
