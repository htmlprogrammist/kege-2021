middle = 10000000

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

primes = []
x = middle
while len(primes) < 3:
  if isPrime(x):
    primes = [x] + primes
  x -= 1
x = middle
while len(primes) < 6:
  if isPrime(x):
    primes.append( x )
  x += 1

for p in primes:
  print( abs(middle-p), p )