"""
Задание 24 (№1273).
Текстовый файл состоит не более чем из 1200000 символов, которые являются прописными буквами латинского алфавита.
Определите максимальное количество идущих подряд символов, среди которых нет подстроки XYZ.
Для выполнения этого задания следует написать программу.
"""
# document = open('24.txt')
# a = document.read()
# m = 0
# k = 0
#
# for i in range(len(a)):
#     if a[i] not in 'XYZ':
#     # if a[i] != 'X' and a[i] != 'Y' and a[i] != 'Z':
#         k += 1
#         m = max(m, k)
#     else:
#         k = 0
# print(m)

f = open('24.txt')
s = f.readline()

curr = 0
m = 0
for i in range(len(s)):
    if s[i] not in 'XYZ':
        curr += 1
        m = max(curr, m)
    else:
        curr = 0
print(m)

