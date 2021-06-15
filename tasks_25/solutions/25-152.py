def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

start, end = 63000000, 75000000
from math import sqrt
for n in range(start, end+1):
  x = n
  while x % 2 == 0: x //= 2
  qX = round(sqrt(sqrt(x)))
  if isPrime(qX) and qX**4 == x:
    print( n, x )