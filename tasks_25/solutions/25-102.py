from math import sqrt

start, end = 268312, 336492

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

count = 0
mi = 1e10
for i in range(start, end+1):
  for x in [2]+list(range(3,round(sqrt(i))+1,2)):
    if i % x == 0 and isPrime(x):
      y = i // x
      if x != y and isPrime(y):
        count += 1
        mi = min(i, mi)
        break

print( count, mi )

