"""
Задание 24 (№865). (А.М. Кабанов) В текстовом файле находится цепочка из символов латинского алфавита A, B, C, D, E, F.
Найдите длину самой длинной подцепочки, не содержащей символов C и F.

19
"""
f = open('24.txt')
s = f.readline()

m = 0
k = 0
for i in range(len(s)):
    if s[i] not in 'CF':
        k += 1
        m = max(m, k)
    else:
        k = 0
print(m)

# k = 1
# max_k = 1
# for i in range(len(s)):
#     if s[i:i+2] != 'CF':
#         k += 1
#         max_k = max(max_k, k)
#     else:
#         k = 1
#         max_k = 1
# print('1-й способ:', max_k)

# k = 0
# max_k = 0
#
# for i in range(len(s) - 1):
#     if s[i] != 'C' and s[i + 1] != 'F':
#         k += 1
#         max_k = max(max_k, k)
#     else:
#         k = 0
#         max_k = 0
# print('3-й способ:', max_k)

# p = s.split('CF')
# m = max(p, key=len)
# print('2-й способ:', len(m) + 1)
#
# # проверка 2-го способа
# s_check = 'EAADEDBBDEAFAADFDFCDBEBEAAFEBFFDAFEAAEDCBEFEEFEEBAEAEFDFEDDCEFEDABBADEEDCAEBFBEFABDDEFABDEACDCDEACABBECDBEDCEFFFEEACABCBDDDABEEBACBBAFCBEEECBCEEFBCDEBDFEAACDEDDABBCDDEFDBFFCDEFEFDFCBBCCDABFBCEEDDFFCCAEEAFAABFAFFDADAECEDBABAEBCDAFEFACCAECCEDBEBBEEDFAAFFEFCAABDCDECBDA'
# for i in range(len(s)):
#     if s[i:i+2] == 'CF':
#         print('Ну ты, конечно, мягко говоря, обосрался')
#         break
