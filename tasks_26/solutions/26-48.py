with open('26-48.txt') as F:
  N = int(F.readline())
  data = [int(s) for s in F]

data.sort()

averages = []
for i in range(N-1):
  for j in range(i+1,N):
    s = data[i] + data[j]
    if s % 2 == 0:
      averages.append( (data[i]+data[j])//2 )
averages.sort()

count, mi = 0, 10**10
i = 0
for avg in averages:
  while i < N and data[i] < avg:
    i += 1
  k = min( avg-data[i-1], data[i]-avg )
  if k == 5:
    count += 1
    mi = min(mi, avg)

print(count, mi)
