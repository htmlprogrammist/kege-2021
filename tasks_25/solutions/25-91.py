from math import sqrt

start, end = 4099, 26985

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

s = 0
qStart = int(sqrt(start))
qEnd = int(sqrt(end))+1
for q in range( qStart, qEnd ):
  x = q*q
  if start <= x <= end and isPrime(q):
    s += sum( map(int, str(x)) )

print(s)
