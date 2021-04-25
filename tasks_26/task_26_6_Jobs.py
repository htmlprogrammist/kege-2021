# https://www.youtube.com/watch?v=dqEglv3sTvo&t=7663s
document = open("txt/task_26_6.txt")
n = int(document.readline())  # прочитал и подчистил за собой эту строку
# Моё почтение, прикольно
a = []
for i in range(n):
    a.append(int(document.readline()))

val = 0
b = 0
m = 25
count = 0

for i in range(1, n - 1):
    if a[i - 1] >= a[i] >= a[i + 1] or a[i + 1] >= a[i] >= a[i - 1]:
        b = a[i]
    elif a[i] >= a[i - 1] >= a[i + 1] or a[i + 1] >= a[i - 1] >= a[i]:
        b = a[i - 1]
    # else:
    elif a[i - 1] >= a[i + 1] >= a[i] or a[i] >= a[i + 1] >= a[i - 1]:
        b = a[i + 1]

    if b < m:
        m = b
        count = 1
    elif b == m:
        count += 1

    if b < a[i]:
        val += a[i] - b

print(count, val)
