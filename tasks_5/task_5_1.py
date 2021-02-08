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


def how_many_units_and_zeros(binary_i):
    global counter_one, counter_zero
    counter_zero = 0
    counter_one = 0
    for j in range(len(binary_i)):
        if binary_i[j] == '1':
            counter_one += 1
        if binary_i[j] == '0':
            counter_zero += 1
    return counter_one, counter_zero


for i in range(0, 256):
    binary_i = bin(i)[2:]  # 1) Строится двоичная запись числа N.

    how_many_units_and_zeros(binary_i)  # 2) К этой записи дописываются разряды по следующему правилу:
    if counter_one > counter_zero:  # а) если единиц больше, чем нулей,
        binary_i += '0'  # в конец дописывается 0,
    else:  # б) иначе
        binary_i = '11' + binary_i  # в начало строки дописывается две 1.

    # print('После первого раза, а потом единицы, а потом нули', binary_i, counter_one, counter_zero)

    how_many_units_and_zeros(binary_i)  # 3) Повторяется пункт 2
    if counter_one > counter_zero:  # а) если единиц больше, чем нулей,
        binary_i += '0'  # в конец дописывается 0,
    else:  # б) иначе
        binary_i = '11' + binary_i  # в начало строки дописывается две 1.

    if int(binary_i, 2) > 500:
        # print(int(binary_i, 2))  # 992
        # print(binary_i)  # 1111100000
        answers.append(i)

# print(answers)  # Ответ по смыслу
print(min(answers))  # Ответ по заданию
