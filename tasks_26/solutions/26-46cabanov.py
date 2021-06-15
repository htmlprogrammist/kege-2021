# Автор: А.М. Кабанов

from bisect import bisect_left

def contains(l, elem):
    index = bisect_left(l,elem)
    if index<len(l):
        return l[index] == elem
    return False

f = open('26-46.txt')
n = int(f.readline())
a = sorted([int(s) for s in f])

count, m = 0, float('inf')
for i in a:
    for j in a:
        for k in a:
            if i<j<k and (i+j+k)%3==0 and contains(a, (i+j+k)//3):
                count+=1
                m = min(m, (i+j+k)//3)
print(count, m)
