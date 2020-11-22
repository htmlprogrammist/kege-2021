document = open('24/24_439.txt')
a = document.read()
k = 0

for i in range(len(a) - 6):
    if a[i] > a[i + 1] < a[i + 2] < a[i + 3] < a[i + 4] < a[i + 5] > a[i + 6]:
        # print(a[i], a[i + 1], a[i + 2], a[i + 3], a[i + 4], a[i + 5], a[i + 6])
        k += 1
print(k)
