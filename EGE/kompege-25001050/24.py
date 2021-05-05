"""
Задание 24 (№887).
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
Определите символ, который чаще всего встречается в файле сразу после буквы X.
В ответе запишите сначала этот символ, а потом сразу (без разделителя)
сколько раз он встретился после буквы X.
Например, в тексте XBCXXBXDDD после буквы X два раза стоит B,
по одному разу – X и D. Для этого текста ответом будет B2.
"""
document = open('24.txt')
a = document.read()
alphabet = []
max_counter = 0
max_counter_index = 0

# chr[65:90]

# Создаю массив с нулями для каждой буквы алфавита
for j in range(26):
    alphabet.append(0)

for i in range(len(a) - 1):
    if a[i] == 'X':
        symbol = ord(a[i + 1])  # Определяю символ
        index = symbol - 65  # Место в алфавите
        alphabet[index] += 1  # Счётчик, сколько раз
# print(alphabet)

for k in range(len(alphabet)):
    if alphabet[k] > max_counter:
        max_counter_index = k
        max_counter = alphabet[k]
print(str(chr(max_counter_index + 65) + str(max_counter)))
