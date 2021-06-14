"""
Задание 24 (№1377).
Текстовый файл состоит не более, чем из 107 символов из набора A, B, C, D, E, F.
Найдите максимальную длину подстроки, в которой ни одна тройка символов не записана два раза подряд.
Например, в искомой подстроке не может быть фрагмента ABCABC.

2278
"""
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
s = 'ABCABC'
i = 0
s[i:i+3]
Out[5]: 'ABC'
s[i+4:i+6]
Out[6]: 'BC'
s[i+3:i+6]
Out[7]: 'ABC'
"""