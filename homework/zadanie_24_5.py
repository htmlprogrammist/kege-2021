document = open('24/24_474.txt')
a = document.read()
current_even_number = ''
k = 0
b = []
max_len_bj = 0

for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        current_even_number += a[i]
    else:
        if current_even_number != '':
            b.append(current_even_number)
        current_even_number = ''
# print(b)

for j in range(len(b)):
    if len(b[j]) > max_len_bj:
        max_len_bj = len(b[j])
print(max_len_bj)
# 18
