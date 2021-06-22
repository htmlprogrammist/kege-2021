"""
№ 1302, Открытый вариант КЕГЭ
Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
Для выполнения этого задания следует написать программу.

1713
"""
f = open('Задание 24/24.txt')
s = f.readline()
s = s.replace('XZZY', 'XZZ XXY')
p = s.split()
m = len(max(p, key=len))
print(m)
f.close()

f = open('Задание 24/24.txt')
s = f.readline()

k = 3
max_k = 3

for i in range(len(s)):
    if s[i:i+4] != 'XZZY':
        k += 1
        max_k = max(k, max_k)
    else:
        k = 3

print(max_k)
