document = open('24/24_223.txt')
a = document.read()
k = 0

for i in range(len(a)-2):
    if (a[i] == 'T' and a[i+1] == 'O' and a[i+2] == 'K') or (a[i] == 'T' and a[i+1] == 'I' and a[i+2] == 'K'):
        k += 1
print(k)  # 31348 С первого раза
