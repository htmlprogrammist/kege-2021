from random import randint
# Уточнить у Савра Владимировича
a = []
n = 30
k = 0
# i, j

for i in range(n):
    a.append(randint(1, 100))
print(a)

for j in range(n):
    if a[j] < 100:
        if a[j] % 2 != 0:
            k += 1
            # a[j] = k -> не совсем понял задание, поэтому второе решение ниже:
print('Количество нечетных чисел меньше 100 =', k)
# Второе решение. Закреплённое количество нечетных чисел меньше 100 заменяется на каждый элемент.
for i in range(n):
    if a[i] < 100 and a[i] % 2 != 0:
        a[i] = k

for j in range(n):
    print(a[j])
