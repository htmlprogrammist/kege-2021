"""
Задание 24 (№934).
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
Определите длину наибольшей последовательности из трех различных символов, расположенным в порядке неубывания.
Например, для строки AABBAABBCCDDDEFFGF такая искомая последовательность BBCCDDD, её длина – 7.

6
"""
f = open('24/24_934.txt')
# s = f.readline()
s = 'AABBAABBCCDDDEFFGF'
#   'A B A B C D E F GF'
#    [2,2,2,2,2,3,1,2,1,1]
# суммарно: мы считаем, сколько раз повторяется та или иная буква и складываем их (1)
# A2 B2 A2 B2 C2 D3 E1 F2 G1 F1

single_string = s[0]  # накапливаем строку, где у нас будут все буквы разные
count_letters = [1]  # накапливаем, сколько букв на каждой позиции соответствуют строке

for i in range(1, len(s)):  # перебираем все символы с первого, т.к. первый уже есть
    if s[i] == s[i - 1]:
        count_letters[-1] += 1  # потому что это та же самая буква
    else:
        single_string += s[i]
        count_letters.append(1)  # новая последовательностьо

print(single_string)
print(count_letters)
max_len = 0

for i in range(len(single_string) - 2):
    if single_string[i] < single_string[i + 1] < single_string[i + 2]:
        sum_letters = count_letters[i] + count_letters[i + 1] + count_letters[i + 2]  # (1)
        if max_len < sum_letters:
            max_len = sum_letters

print(max_len)

# document = open('24/24_934.txt')
# a = document.read()
# a = 'AABBAABBCCDDDEFFGF'
# k = 0
# max_k = 0
# symbols = set()
# prev = 0

# for i in range(len(a)):
#     if prev <= ord(a[i]) and len(symbols) < 3:
#         k += 1
#         if a[i] not in symbols:
#             symbols.add(a[i])
#         if k > max_k:
#             max_k = k
#         prev = ord(a[i])
#         print('Symbols: {0}, k = {1}, max_k = {2}, a[i] = {3}, previous = {4}'.format(symbols, k, max_k, a[i], prev))
#     else:
#         k = 0
#         symbols = set()
#         prev = 0

# он не сбрасывает значение для предыдущего элемента, поэтому решение с двумя циклами - не самая лучшая идея
# или надо продумать как-то, чтобы он всё-таки научился его изменять
# for i in range(len(a) - 1):
#     # a[i] == prev
#     s = a[i]
#     for j in range(1, len(a)):
#         if prev <= ord(a[j]) and len(symbols) < 3:
#             k += 1
#             prev = ord(a[j])
#             if k > max_k:
#                 max_k = k
#             if a[j] not in symbols:
#                 symbols.add(a[j])
#             print(
#                 'Symbols: {0}, k = {1}, max_k = {2}, cur_elem = {3}, previous = {4}'.format(symbols, k, max_k, a[j], a[i]))
#         else:
#             k = 1
#             symbols = set()
#             s = ''
#             prev = 0
#
# print(max_k)
