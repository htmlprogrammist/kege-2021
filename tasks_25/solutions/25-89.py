start, end = 2948, 20194

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

for x in range( end, start-1, -1 ):
  if isPrime(x):
    print(x)
    break
