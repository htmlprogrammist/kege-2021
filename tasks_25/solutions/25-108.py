from math import sqrt

start, end = 238941, 315675

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

iMaxDiff = []
maxDiff = 0
count = 0
for i in range(start, end+1):
  q = round(sqrt(i))
  D = [2] + list( range(3, q+1, 2) )
  for x in D:
    if i % x == 0 and isPrime(x):
      y = i // x
      if x != y and isPrime(y):
        count += 1
        if (y - x) > maxDiff:
          maxDiff = y - x
          iMaxDiff = i
        break

print( count, iMaxDiff )

