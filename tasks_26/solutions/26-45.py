with open('26-45.txt') as F:
  N = int(F.readline())
  data = [int(s) for s in F]

who = dict( zip(data, [1 for i in range(N)]) )

count, ma = 0, 0
for i in range(N):
  for j in range(i+1,N):
    s = data[i] + data[j]
    if s % 2 == 0 and s//2 in who:
      count += 1
      ma = max( ma, s//2 )

print(count, ma)
