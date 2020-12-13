a = [5.2, 13.1, 2.2, 12.3, 3.1, 2.3]
# a = [13.1, 5.2, 2.2, 12.3, 3.1, 2.3] = ответ не меняется
max_a = -10

for i in range(len(a) - 1):
    if abs(a[i]) - abs(a[i + 1]) <= 10:
        if max_a < a[i] + a[i + 1]:
            max_a = a[i] + a[i + 1]
print(int(max_a))
