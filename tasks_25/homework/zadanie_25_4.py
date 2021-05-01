from random import randint

a = []
n = 30
k = 0
# i, j

for i in range(0, n):
    a.append(randint(-10000, 10000))
print(a)

for j in range(0, n-1):
    if (a[j] % 7 != 0 and a[j+1] % 7 == 0) or (a[j] % 7 == 0 and a[j+1] % 7 != 0):
        k += 1
print(k)
