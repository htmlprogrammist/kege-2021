# s = 'OASDAAFGAAHJO'
# # s = 'NOTEBOOK'  # 2 и 7-ой. 6-ая О не учитывается, т.к. есть 7-ая
# index = 0
# a = []
# max_d = 0
# for j in range(len(s) - 1):
#     for k in range(1, len(s)):
#         if s[j] == s[k]:
#             distance = k - j
#             if max_d < distance:
#                 max_d = distance
# print(max_d)

document = open('24_example.txt')
a = document.readlines()
distance = 0
max_distance = 0

for i in range(len(a)):
    if a[i].count('G') < 25:
        for j in range(len(a[i]) - 1):
            for k in range(1, len(a[i])):
                if a[i][j] == a[i][k]:
                    distance = k - j
                    if max_distance < distance:
                        max_distance = distance
print(max_distance)
