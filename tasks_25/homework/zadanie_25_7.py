# k = max
from random import randint

a = []
n = 30
k = -1001
# i, j

for i in range(n):
    a.append(randint(-1000, 1000))
print(a)
# a.append(-3)
# a.append(-2)
# a.append(-7)
# a.append(-4)

for j in range(n):
    if (a[j] % 10 == 3) and (a[j] > 0): # Видимо, из-за "<" получается так, что ответ не совпадает и надо писать
    # if (a[j] < 0) and (a[j] % 10 == 7):  # деление на 7, а не на 3. Если поставить 3, то числа оканчиваются на 3
        print(a[j])
        if a[j] > k:
            k = a[j]

if k == -1001:
    print('Не найдено')
else:
    print(k)
