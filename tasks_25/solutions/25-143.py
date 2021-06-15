s, e = 33333, 55555

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

def sumDigits( x ):
  return sum( map(int, str(x)) )

for x in range(s, e+1):
  if isPrime(x):
    s = sumDigits(x)
    if s > 35:
      print( x, s )

