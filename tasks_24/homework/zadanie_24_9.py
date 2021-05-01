document = open('24_66.txt')
a = document.read()
k = 1

for i in range(len(a)-5):
    if a[i] == 'К' and a[i+1] == 'О' and a[i+2] == 'Т':
        if a[i + 3] == 'К' and a[i + 4] == 'О' and a[i + 5] == 'Т':
            k += 1
print(k)
# 75
