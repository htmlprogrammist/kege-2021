with open("26-42.txt") as F:
  N, S = map(int, F.readline().split())

  data = []
  for i in range(N):
    model, price, size = F.readline().split()
    data.append( (model, int(price), int(size) ) )

data.sort( key = lambda d: (d[0], d[1]) )

xSum = 0
countZ = 0
for d in data:
  if xSum+d[1] > S: break
  thisCount = min(d[2], int((S-xSum)/d[1]))
  print( d, '+' + str(thisCount) )
  xSum += d[1]*thisCount
  if d[0] == 'Z':
    countZ += thisCount

print( countZ, S-xSum )





