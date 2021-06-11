"""
Задание 24 (№439).
Текстовый файл состоит не более чем из 106 десятичных цифр.
Восходящей последовательностью называется последовательность цифр, в которой каждая цифра меньше следующей за ней.
Например, в последовательности 7238903278 три таких последовательности – 2389, 03 и 278.
Длиной последовательности называется количество входящих в нее цифр.
Определите сколько в файле восходящих последовательностей длиной 5,
не входящих в восходящие последовательности большей длины.
Для выполнения этого задания следует написать программу.

2278
"""
# NB! Сейчас здесь не тот файлик, потому что компегэ сейчас (11.06.2021 10:34) пребывает в странном состоянии
f = open('24.txt')
s = f.readline()

cur_l = 5
max_l = 5

for i in range(len(s) - 5):
    if s[i:i+3] != s[i+3:i+6]:
        cur_l += 1
    else:
        cur_l = 5
    max_l = max(cur_l, max_l)

print(max_l)

"""
i = 0
s[i:i+3]
Out[5]: 'ABC'
s[i+4:i+6]
Out[6]: 'BC'
s[i+3:i+6]
Out[7]: 'ABC'
"""
