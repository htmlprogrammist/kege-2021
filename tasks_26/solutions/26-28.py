with open("26-j3.txt") as F:
  S, N = map( int, F.readline().split() )
  data = []
  for i in range(N):
    x = int(F.readline())
    data.append( x )

data.sort( reverse = True )

count = 0
minSize = 10**9
for x in data:
  if S >= x:
    S -= x
    minSize = x
    count += 1

print( count, minSize )