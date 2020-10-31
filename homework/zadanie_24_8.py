document = open('24/24_414.txt')
a = document.read()
k1 = 0
k2 = 0

for i in range(len(a)-2):
    if a[i] == 'R' and a[i+1] == 'U' and a[i+2] == 'S':
        k1 += 1

for i in range(len(a)-5):
    if a[i] == 'R' and a[i + 1] == 'U' and a[i + 2] == 'S' and a[i + 3] == 'T' and a[i + 4] == 'E' and a[i + 5] == 'M':
        k2 += 1

print(k1-k2)  # 4611
# Почти с первого раза. Ошибка была по невнимательности
