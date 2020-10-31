from random import randint

a = []
n = 30
k = 0
for i in range(n):
    a.append(randint(-10000, 10000))
print(a)

for j in range(0, n-1):
    if ((a[j] + a[j+1]) % 7 == 0) and ((a[j] + a[j+1]) < 0):
        k+=1
        # print(a[j], a[j+1])
print(k)
