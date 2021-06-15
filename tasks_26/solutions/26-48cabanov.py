# Автор: А.М. Кабанов

from bisect import bisect_left

def minDiff(l, elem):
    index = bisect_left(l,elem)
    return min(l[index]-elem, elem - l[index-1])

f = open('26-48.txt')
n = int(f.readline())
a = sorted([int(s) for s in f])

count, m = 0, float('inf')
for i in a:
    for j in a:
        k = minDiff(a, (i+j)//2)
        if i<j and (i+j)%2==0 and k==5:
            count+=1
            m = min(m, (i+j)//2)
print(count, m)
