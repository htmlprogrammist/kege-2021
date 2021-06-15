from math import sqrt

start, end = 153732, 225674

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

iMinDiff = []
minDiff = 1e10
count = 0
for i in range(start, end+1):
  q = round(sqrt(i))
  D = [2] + list( range(3, q+1, 2) )
  for x in D[::-1]:
    if i % x == 0 and isPrime(x):
      y = i // x
      if x != y and isPrime(y):
        count += 1
        if (y - x) < minDiff:
          minDiff = y - x
          iMinDiff = i
        break

print( count, iMinDiff )

