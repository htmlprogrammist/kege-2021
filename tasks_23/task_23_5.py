# +1 *2
k = [1] * 11
for n in range(1, 10 + 1):
    k[n] = k[n - 1]
    if n % 2 == 0:
        k[n] += k[n // 2]
print(k[10])

k = [0] * 11
k[1] = 1
for n in range(1, 10 + 1):
    if (n + 1) <= 10:
        k[n + 1] += k[n]
    if (n * 2) <= 10:
        k[n * 2] += k[n]
print(k)
print(k[10])
