def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

start, end = 103000000, 104000000
from math import ceil, sqrt
for x in range(ceil(sqrt(start//2)), ceil(sqrt(end//2))):
  if isPrime(x):
    n = 2*x*x;
    print( n, x )