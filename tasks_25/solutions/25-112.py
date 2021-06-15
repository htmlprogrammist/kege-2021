from math import sqrt

start, end = 298435, 363249

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

s = 0
count = 0
allX = []
for i in range(start, end+1):
  q = round(sqrt(i))
  D = [2] + list( range(3, q+1, 2) )
  for x in D:
    if i % x == 0 and isPrime(x):
      y = i // x
      if x != y and isPrime(y):
        count += 1
        s += i
        allX.append( i )
        break

average = s / count
diff = [ abs(x-average) for x in allX]
minDiff = min(diff)
ind = diff.index( minDiff )

print( count, allX[ind] )

