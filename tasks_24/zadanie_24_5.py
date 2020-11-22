document = open('homework/24/24_279_1.txt')
a = document.read()
k = 0

for i in range(len(a) - 5):
    if a[i] != 'J' and a[i + 5] != 'J' and a[i + 1] == 'B' and a[i + 2] == 'O' and a[i + 3] == 'S' and a[i + 4] == 'S':
        print(a[i], a[i + 1], a[i + 2], a[i + 3], a[i + 4], a[i + 5])
        k += 1
print(k)
