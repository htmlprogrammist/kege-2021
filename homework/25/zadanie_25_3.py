from random import randint

a = []
n = 40
k = 0
# i, j

for i in range(0, n):
    a.append(randint(0, 10000))
print(a)

for j in range(0, n-2):
    if ((a[j] + a[j + 1] + a[j + 2]) % 2 == 0) or (a[j] > a[j+1]):
        k += 1
print(k)
