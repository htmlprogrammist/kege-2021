s, e = 33333, 55555

def allDivs( x ):
  divs = [1, x]
  d = 2
  while d*d <= x:
    if x % d == 0:
      divs.append( d )
      if x // d > d:
        divs.append( x//d )
    d += 1
  return sorted(divs)

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

def isValid( x ):
  primeDivs = [d for d in allDivs(x)[1:-1] if isPrime(d)]
  s = sum(primeDivs)
  if s > 250 and x % s == 0:
    return s
  else:
    return 0

for x in range(s, e+1):
  s = isValid(x)
  if s > 0:
    print( x, s )

