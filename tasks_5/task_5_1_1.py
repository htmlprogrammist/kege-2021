"""
№ 350
На вход алгоритма подаётся натуральное число N.
Алгоритм строит по нему новое число R следующим образом.
1) Строится двоичная запись числа N.
2) К этой записи дописываются разряды по следующему правилу:
а) если единиц больше, чем нулей, в конец дописывается 0,
б) иначе в начало строки дописывается две 1.
3) Повторяется пункт 2
Полученная таким образом запись является двоичной записью искомого числа R.
Укажите минимальное число N, при вводе которого получится значение R больше, чем 500.
В ответе полученное число запишите в десятичной системе.

32
"""

answers = []

for i in range(0, 256):
    binary_i = bin(i)[2:]

    counter_zero = 0
    counter_one = 0
    for j in range(len(binary_i)):
        if binary_i[j] == '1':
            counter_one += 1
        if binary_i[j] == '0':
            counter_zero += 1
    if counter_one > counter_zero:
        binary_i += '0'
    else:
        binary_i = '11' + binary_i

    counter_zero = 0
    counter_one = 0
    for j in range(len(binary_i)):
        if binary_i[j] == '1':
            counter_one += 1
        if binary_i[j] == '0':
            counter_zero += 1
    if counter_one > counter_zero:
        binary_i += '0'
    else:
        binary_i = '11' + binary_i

    if int(binary_i, 2) > 500:
        # print(int(binary_i, 2))  # 992
        # print(binary_i)  # 1111100000
        answers.append(i)

# print(answers)  # Ответ по смыслу
print(min(answers))  # Ответ по заданию
