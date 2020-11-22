from random import randint
k = 0
n = 40
a = []
# i, j

for i in range(0, n):
    a.append(randint(0, 10000))
print(a)
for j in range(len(a)-1):
    if (a[j] < a[j+1]) and (a[j] % 5 == 0):
        k += 1
print(k)
