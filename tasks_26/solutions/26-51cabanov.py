# Автор: А.М. Кабанов

f = open('26-51.txt')
n = int(f.readline())
a = sorted([int(s) for s in f])

count, m = 0, 0
for i in range(len(a)-1):
  for j in range(i+1,len(a)):
     if (j-i)>=101 and (a[i]+a[j])%2==0:
        count+=1
        m = max(m, (a[i]+a[j])//2)
print(count, m)
