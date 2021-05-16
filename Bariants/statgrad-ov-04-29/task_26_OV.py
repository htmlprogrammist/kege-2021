f = open('26.txt')
n = int(f.readline())
chet = []
nechet = []
for i in range(n):
    a = int(f.readline())
    if a % 2 == 0:
        chet.append(a)
    else:
        nechet.append(a)
cn = set(chet)
nn = set(nechet)
max_s = 0
k = 0
for i in range(len(chet)):
    for j in range(len(nechet)):
        b = chet[i] + nechet[j]
        if b in cn or b in nn:
            k += 1
            if b > max_s:
                max_s = b
print(k, max_s)
