document = open('homework/24/24_279_1.txt')
a = document.read()
k = 0

for i in range(len(a)-5):
    if a[i] != 'J' and a[i+1] == 'B' and a[i+2] == 'O' and a[i+3] == 'S' and a[i+4] == 'S' and a[i+5] != 'J':
        k += 1
print(k)  # 2198
