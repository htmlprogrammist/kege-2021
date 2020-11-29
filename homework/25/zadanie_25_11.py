from random import randint

a = []
n = 30
k = 0
# i, j

for i in range(n):
    a.append(randint(1, 10000))
print(a)

for j in range(n):
    if a[j] > 80:
        if a[j] % 10 == 1:
            k += 1
print('Количество элементов =', k)
for i in range(n):
    if a[i] > 80:
        if a[i] % 10 == 1:
            # print('Элемент до увеличения на К', a[i])
            a[i] += k

for j in range(n):
    print(a[j])
