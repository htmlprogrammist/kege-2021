"""
Алгоритм получает на вход натуральное число N > 1 и строит по нему новое
число R следующим образом:
1. Строится двоичная запись числа N.
2. Подсчитывается количество нулей и единиц в полученной записи. Если их
количество одинаково, в конец записи добавляется её последняя цифра.
В противном случае в конец записи добавляется та цифра, которая
встречается реже.
3. Шаг 2 повторяется ещё два раза.
4. Результат переводится в десятичную систему счисления.
При каком наименьшем исходном числе N > 99 в результате работы
алгоритма получится число, кратное 4?

103
"""
for i in range(100, 1000):
    binary = bin(i)[2:]
    units = binary.count('1')
    zeroes = binary.count('0')
    if units == zeroes:
        binary += binary[-1]
    else:
        if units < zeroes:
            binary += '1'
        else:
            binary += '0'
    '''---'''
    units = binary.count('1')
    zeroes = binary.count('0')
    if units == zeroes:
        binary += binary[-1]
    else:
        if units < zeroes:
            binary += '1'
        else:
            binary += '0'
    '''---'''
    units = binary.count('1')
    zeroes = binary.count('0')
    if units == zeroes:
        binary += binary[-1]
    else:
        if units < zeroes:
            binary += '1'
        else:
            binary += '0'
    if int(binary, 2) % 4 == 0:
        print(i)
        break
