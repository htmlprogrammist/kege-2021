with open('26-46.txt') as F:
  N = int(F.readline())
  data = [int(s) for s in F]

who = dict( zip(data, [1 for i in range(N)]) )

count, mi = 0, 10**10
for i in range(N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      s = data[i] + data[j] + data[k]
      if s % 3 == 0 and s//3 in who:
        count += 1
        mi = min( mi, s//3 )

print(count, mi)
