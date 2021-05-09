"""
Задание 24 (№1273).
Текстовый файл состоит не более чем из 1200000 символов, которые являются прописными буквами латинского алфавита.
Определите максимальное количество идущих подряд символов, среди которых нет подстроки XYZ.
Для выполнения этого задания следует написать программу.

305
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
s = s.replace('XYZ', 'XY YZ')
s_max = max(s.split(), key=len)  # key=len - поиск по длине
print(len(s_max))
