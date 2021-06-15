# Автор: А.М. Кабанов

from bisect import bisect_left

def smaller(l, elem):
    index = bisect_left(l,elem)
    return index

f = open('26-47.txt')
n = int(f.readline())
a = sorted([int(s) for s in f])

count, m = 0, 0
for i in a:
    for j in a:
        k = smaller(a, (i+j)/2)
        if i<j and k>0 and k%100==0:
            count+=1
            m = max(m, k)
print(count, m)
