from math import sqrt

start, end = 158928, 345293

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

count = 0
mi = 0
for i in range(start, end+1):
  q = round(sqrt(i))
  Dx = [2] + list( range(3, q+1, 2) )
  found = False
  for x in Dx:
    if i % x == 0 and isPrime(x):
      yz = i // x
      qyz = round(sqrt(yz))
      for y in range(x+1,qyz+1):
        if yz % y == 0 and isPrime(y):
          z = yz // y
          found = True
          if z != y and z != x and isPrime(z):
            count += 1
            if mi == 0:
              mi = i
          break
      if found: break

print( count, mi )

