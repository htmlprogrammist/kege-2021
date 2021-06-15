# Автор: А.М. Кабанов

from bisect import bisect_left

def isSmaller(l, elem):
    index = bisect_left(l,elem)
    if elem<l[index]: index-=1
    return index < len(l)//2

f = open('26-49.txt')
n = int(f.readline())
a = sorted([int(s) for s in f])

count, m = 0, 0
for i in a:
    for j in a:
        if i<j and (i+j)%2==0 and isSmaller(a, (i+j)//2):
            count+=1
            m = max(m, (i+j)//2)
print(count, m)
