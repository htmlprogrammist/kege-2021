""" OV 24 задание
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
Определите символ, который чаще всего встречается в файле сразу после буквы A.
Например, в тексте ABCAABADDD после буквы A два раза стоит B, по одному разу – A и D.
Для этого текста ответом будет B.
AB, AA, AB, AD считаются
"""

document = open('22.txt')
a = document.read()
alphabet = []
max_counter = 0
max_counter_index = 0

# chr[65:90]

# Создаю массив с нулями для каждой буквы алфавита
for j in range(26):
    alphabet.append(0)

for i in range(len(a) - 1):
    if a[i] == 'A':
        symbol = ord(a[i + 1])  # Определяю символ
        index = symbol - 65  # Место в алфавите
        alphabet[index] += 1  # Счётчик, сколько раз
# print(alphabet)

for k in range(len(alphabet)):
    if alphabet[k] > max_counter:
        max_counter_index = k
        max_counter = alphabet[k]
print(chr(max_counter_index + 65))
# print(max_counter == max(alphabet)) Проверка, совпадают ли значения максимума через функцию Питона
# и то, как я нашёл максимум
