"""
№ 1233, Апробация 27.04
Имеется набор данных, состоящий из N троек натуральных чисел. Составьте сумму из N чисел,
выбрав из каждой тройки ровно одно число так, чтобы эта сумма не делилась нацело на k = 101
и была максимально возможной. Гарантируется, что искомую сумму получить можно.
Входные данные:
Даны два входных файла (файл А и файл В),
каждый из которых содержит в первой строке количество троек N (1 ≤ N ≤ 1000000).
Каждая из следующих N строк содержит три натуральных числа, не превышающих 10000.
Пример организации исходных данных во входном файле:
6
1 3 7
5 12 6
6 9 11
5 4 8
3 5 4
1 1 1
Для указанных входных данных в случае, если k = 5, искомой суммой является число 44.
В ответе укажите два числа: значение искомой суммы сначала для файла A, затем для файла B.

694390 7567616720
"""
f = open("27_B-1.txt")
n = int(f.readline())
s = [0]
for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    cmb = [a + b for a in s for b in pair]
    s = {x % 101: x for x in sorted(cmb)}.values()

m = max(x for x in s if x % 101 != 0)
print(m)
