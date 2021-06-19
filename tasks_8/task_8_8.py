"""
№ 1688
Ксения составляет слова из букв К, С, Е, Н, И, Я. Каждая гласная буква встречается в слове не более двух раз.
Каждая согласная может стоять в слове на первой позиции, либо не встречаться вовсе.
Сколько слов длиною более двух символов может составить Ксения?

1059
"""
from itertools import product

# p = product('КСЕНИЯ', repeat=6)
# s = map(lambda x: "".join(x), p)
counter1 = 0
counter2 = 0
words = []
more_words = []
for length in range(3, 6 + 1):
    p = product('КСЕНИЯ', repeat=length)
    s = map(lambda x: "".join(x), p)
    for i in s:
        if i.count('Е') <= 2 and i.count('И') <= 2 and i.count('Я') <= 2:
            if i[0] == 'К' or i[0] == 'С' or i[0] == 'Н':
                flag = True
                for symbol in i[1:]:
                    if symbol == 'К' or symbol == 'С' or symbol == 'Н':
                        flag = False
                if flag:
                    words.append(i)
                    counter1 += 1
print(counter1)
print(words)

for length in range(3, 6 + 1):
    p = product('ЕИЯ', repeat=length)  # согласная не встречается вовсе
    s = map(lambda x: "".join(x), p)
    for i in s:
        if i.count('Е') <= 2 and i.count('И') <= 2 and i.count('Я') <= 2:
            counter2 += 1
            more_words.append(i)
# print(counter1 + counter2)  # 789
print(counter2)
print(more_words)
