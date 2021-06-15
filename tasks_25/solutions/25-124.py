from math import sqrt

start, end = 536792, 604298

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

count = 0
maxDiff = 0
iMaxDiff = 0
for i in range(start, end+1):
  q = round(sqrt(i))
  Dx = [2] + list( range(3, q+1, 2) )
  found = False
  for x in Dx:
    if i % x == 0 and isPrime(x):
      yz = i // x
      qyz = round(sqrt(yz))
      for y in range(x+1,qyz+1):
        if yz % y == 0 and isPrime(y) and (x % 10 == y % 10):
          z = yz // y
          found = True
          if z != y and z != x and isPrime(z) and (x % 10 == z % 10):
            count += 1
            if z - x > maxDiff:
              maxDiff = z - x
              iMaxDiff = i
          break
      if found: break

print( count, iMaxDiff )

