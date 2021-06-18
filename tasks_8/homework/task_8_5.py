"""
Все 4-буквенные слова, составленные из букв К, Л, Р, Т, записаны в алфавитном порядке и пронумерованы.
Вот начало списка:
1. КККК
2. КККЛ
3. КККР
4. КККТ
…
Запишите слово, которое стоит на 67-м месте от начала списка.
"""
from itertools import product

p = product('КЛРТ', repeat=4)
counter = 0
s = list(map(lambda x: "".join(x), p))
count = 1
for i in s:
    print(count, s[count - 1])
    count += 1
