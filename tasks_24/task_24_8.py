"""
Задание 24 (№934).
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
Определите длину наибольшей последовательности из трех различных символов, расположенным в порядке неубывания.
Например, для строки AABBAABBCCDDDEFFGF такая искомая последовательность BBCCDDD, её длина – 7.
"""
document = open('24/24_934.txt')
# a = document.read()
a = 'AABBAABBCCDDDEFFGF'
k = 0
max_k = 0
symbols = set()
prev = 0

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
# TODO Научить этот алгоритм останавливаться, когда он встретил символ, орд которого больше его самого
for i in range(len(a) - 1):
    # a[i] == prev
    s = a[i]
    for j in range(1, len(a)):
        if ord(a[i]) <= ord(a[j]) and len(symbols) < 3:
            k += 1
            s += a[j]
            print(s)
            # if k > max_k:
            #     max_k = k
            # if a[j] not in symbols:
            #     symbols.add(a[j])
            # print(
            #     'Symbols: {0}, k = {1}, max_k = {2}, cur_elem = {3}, previous = {4}'.format(symbols, k, max_k, a[j], a[i]))
        else:
            break

print(max_k)