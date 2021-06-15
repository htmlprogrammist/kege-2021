from math import sqrt

start, end = 194441, 196500

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

qStart = int(sqrt(start))
qEnd = int(sqrt(end)) + 1

i = 0
for q in range( qStart, qEnd+1 ):
  x = q*q
  if start <= x <= end:
    divs = allDivs(x)
    i += 1
    print( i, x, len(divs), q )



