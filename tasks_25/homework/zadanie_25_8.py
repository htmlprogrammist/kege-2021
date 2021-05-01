from random import randint

a = []
n = 30
k = 10000
# i, j

# Проверка
# n = 24
# a.append(9990)
# a.append(20)
# a.append(40)
# a.append(30)

for i in range(n):
    a.append(randint(1, 10000))
print(a)

for j in range(n):
    if a[j] % 10 == 0:
        if a[j] < k:
            k = a[j]
            # print('Мы нашли минимум', k)
        else:
            a[j] = k
            # print('Индекс элемента', j)

for i in range(n):
    print(a[i])
