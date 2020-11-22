from random import randint

a = []
n = 40
k = 0
for i in range(0, n):
    a.append(randint(0, 10000))
print(a)

for j in range(0, n-1):
    if (a[j] % 100 == 10) or (a[j+1] % 100 == 10):
        k += 1
print(k)
