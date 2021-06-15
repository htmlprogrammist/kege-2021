# Автор: А.М. Кабанов

F = open('26-52.txt')
N = int(F.readline())
data = sorted( [int(s) for s in F] )

gap = 100

count, ma = 0, float('inf')
for i in range(N-1):
  for j in range(i+1,i+gap+2):
    if j < N and (data[i] + data[j]) % 10 == 0:
      count += 1
      ma = min( ma, (data[i]+data[j])//2 )

print(count, ma)
