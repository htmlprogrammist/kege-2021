"""
Задание 5 (№559).
На вход алгоритма подаётся натуральное число N.
Алгоритм строит по нему новое число следующим образом.
1) Строится двоичная запись числа N.
2) К этой записи дописываются справа ещё два разряда по следующему правилу:
если N чётное, в конец числа (справа) дописываются два нуля,
в противном случае справа дописываются две единицы.
Например, двоичная запись 1001 числа 9 будет преобразована в 100111.
Полученная таким образом запись
(в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью числа – результата работы данного алгоритма.
Укажите минимальное число N, для которого результат работы алгоритма будет больше 115.
В ответе это число запишите в десятичной системе счисления.

29
"""
# 115 в двоичном представлении будет равняться 1110011
# Поскольку длина здесь равняется 7, а прибавляем мы два разряда => максимальное число 31
condition = 115
mx = 0

for N in range(32):
    binary = bin(N)[2:]
    if N % 2 == 0:
        binary += '00'
    else:
        binary += '11'
    # print(binary, answer)
    if int(binary, 2) > condition:
        print(N)
        break
