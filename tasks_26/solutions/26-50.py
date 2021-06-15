with open('26-50.txt') as F:
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
      #print( data[i], data[j], s//2 )
      averages.append( s//2 )
averages.sort()

borderLeft = data[N//2-1]
borderRight = data[3*N//4]
selected = [x for x in averages
              if borderLeft < x < borderRight];

print( len(selected), selected[0] )
