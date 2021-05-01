from random import randint

a = []
k = 0
# i, j
n = 40
# a.append(2)
# a.append(2)
# a.append(2)

# for i in range(4, n):
for i in range(n):
    a.append(randint(0, 10000))
print(a)

for j in range(len(a) - 1):
    if a[j] == a[j + 1] == a[j + 2]:
        k += 1

print(k)