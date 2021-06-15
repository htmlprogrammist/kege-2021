with open('26-49.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    data.append( int(F.readline()) )
  #data = [int(s) for s in F]

data.sort()

averages = []
for i in range(N-1):
  for j in range(i+1,N):
    s = data[i] + data[j]
    if s % 2 == 0:
      averages.append( s//2 )
averages.sort()

medianRight = data[N//2]
selected = [x for x in averages if x < medianRight];

print( len(selected), selected[-1] )
