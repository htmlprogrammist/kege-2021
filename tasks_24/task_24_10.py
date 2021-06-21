"""
Определите максимальное количество идущих подряд символов, среди которых символ Z встречается не более одного раза.
"""
f = open('24/24_1144.txt')  # file не тот
s = f.readline()

k = 0
kmax = 0  # max количество идущих подряд символов
z0 = 0

for i in range(len(s)):
    if s[i] == 'Z':
        z0 += 1
        if z0 < 2:
            k += 1
            kmax = max(k, kmax)
        elif z0 >= 2:
            k = 0
            z0 = 0
    else:
        k += 1
        kmax = max(k, kmax)
print(kmax)
