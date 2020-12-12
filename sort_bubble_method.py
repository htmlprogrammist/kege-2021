# Алгоритм сортировки - метод пузырька
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for j in range(len(a) - 1):
    for k in range(j + 1, len(a)):
        if a[j] < a[k]:
            a[j], a[k] = a[k], a[j]
print('Второй максимум среди элементов массива', a[1])
# ИЛИ
#         if a[j] > a[k]:
#             a[j], a[k] = a[k], a[j]
# print('Второй максимум среди элементов массива', a[-2])
print(a)
