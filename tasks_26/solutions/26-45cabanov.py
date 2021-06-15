# Автор: А.М. Кабанов

from bisect import bisect_left

def contains(l, elem):
    return elem in l
    index = bisect_left(l,elem)
    if index<len(l):
        return l[index] == elem
    return False

f = open('26-45.txt')
n = int(f.readline())
a = sorted([int(s) for s in f])

count, m = 0, 0
for i in a:
    for j in a:
        if i<j and (i+j)%2==0 and contains(a, (i+j)//2):
            count+=1
            m = max(m, (i+j)//2)
print(count, m)
