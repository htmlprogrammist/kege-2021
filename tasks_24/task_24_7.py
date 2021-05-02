"""
№ 1064, Джобс 15.03.2021
Текстовый файл состоит из множества строк, каждая из которых может содержать буквы из набора A, B, C, D, E, F.
1) Для каждой строки необходимо найти максимальную длину подстроки, состоящей из одинаковых символов.
2) Для всего файла необходимо определить, какая буква чаще всего образует подстроки максимальной длины,
найденные в предыдущем пункте.
Если в строке несколько подстрок из различных букв, то считается,
что каждая из этих букв составляет подстроку максимальной длины.
Например, в строке AABBBBBDDCCCCCE, будет две буквы, составляющих подстроки максимальной длины – B и C.
В качестве ответа необходимо вывести буквы, которые чаще всего составляют подцепочки максимальной длины

A
"""
document = open('24/24_1064.txt')
letters = []
for line in document:
    cur_letters = set()
    cur_len = 0
    max_len = 1
    previous = ' '
    for symbol in line:
        if previous == symbol:
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
                cur_letters = set(symbol)
            elif max_len == cur_len:
                cur_letters.add(symbol)
        else:
            cur_len = 1
        previous = symbol
    letters = letters + list(cur_letters)

for i in set(letters):
    print(i, letters.count(i))
