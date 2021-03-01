# 3 => 15 и проходит через 10
k = [1] * 16
k[3] = k[4] = 1
for i in range(5, 11):
    k[i] = k[i - 1] + k[i - 2]
print(k[10])  # 21

for i in range(11, 16):
    k[i] = k[i - 1]
    if i > 11:
        k[i] += k[i - 2]
    # k[i] = k[i - 1] + k[i - 2]
print(k[15])  # 68
