"""
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z).
Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.
Например, в тексте CBCABABACCC есть комбинации CBC, ABA (два раза), BAB и CCC.
Чаще всего – 3 раза – между двумя одинаковыми символами стоит B,
в ответе для этого случая надо написать B.
"""

document = open('Faily_IN11_02022021/24/24_2010301_statgrad.txt')
a = document.read()
alphabet = []
max_k = 0
max_k_index = 0

for i in range(26):
    alphabet.append(0)

for i in range(1, len(a) - 1):
    if a[i-1] == a[i + 1]:
        index = ord(a[i]) - 65
        alphabet[index] += 1

for i in range(len(alphabet)):
    if alphabet[i] > max_k:
        max_k = alphabet[i]
        max_k_index = i

print(chr(max_k_index + 65))
