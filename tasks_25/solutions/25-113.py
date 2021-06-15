from math import sqrt

start, end = 309829, 365874

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

divs = []
minDiff = 1e10
for i in range(start, end+1):
  q = round(sqrt(i))
  D = [2] + list( range(3, q+1, 2) )
  for x in D[::-1]:
    y = i // x
    if (y - x) >= minDiff: break
    if i % x == 0 and isPrime(x):
      if x != y and isPrime(y) and (y - x) < minDiff:
        minDiff = y - x
        divs = [x, y]
      break

print( divs[0], divs[1] )

