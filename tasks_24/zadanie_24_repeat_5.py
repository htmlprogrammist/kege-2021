document = open('24/24_66.txt')
a = document.read()
k = 0
i = 0

while i < len(a):
    if a[i] == 'K' and a[i+1] == 'О' and a[i+2] == 'Т':
        k += 1
        i += 3
    else:
        i += 1
print(k)
