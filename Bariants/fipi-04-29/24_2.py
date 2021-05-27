document = open("Задание 24/24.txt")
a = document.readline()
mx = 3
counter = 3
for i in range(len(a) - 4):
    if a[i:i+4] != 'XZZY':
        counter += 1
        mx = max(mx, counter)
    else:
        counter = 3
print(mx)  # 1713
