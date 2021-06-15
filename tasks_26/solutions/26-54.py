with open('26-53.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
     data.append( int(F.readline()) )
  #data = [int(s) for s in F]

data.sort()
print(data)

averages = []
for i in range(N-1):
  for j in range(i+1,N):
    if data[i] % 2 == 0 and data[j] % 2 == 0:
      s = data[i] + data[j]
      print( data[i], data[j], s//2 )
      averages.append( s//2 )
averages.sort()

selected = []
i = 0
for av in averages:
  while i < N and data[i] < av:
    i += 1
  if i < N and data[i] == av:
    selected.append(av)

print( len(selected), selected[0] )
