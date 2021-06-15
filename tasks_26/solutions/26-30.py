with open("26-j5.txt") as F:
  n = int( F.readline() )
  data = []
  for i in range(n):
    x = int(F.readline())
    data.append( x )

def middle( a, b, c ):
  abc = sorted( [a, b, c] )
  return abc[1]

modified = data[:]
fillOut = 0
for i in range(1, n-1):
  modified[i] = middle( data[i-1], data[i], data[i+1])
  fillOut += max(0, data[i] - modified[i] )

print( modified.count(min(modified)),
       fillOut )