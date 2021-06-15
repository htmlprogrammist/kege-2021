from math import sqrt

start, end = 573213, 575340

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
minSum = 1e10
minDivs = []
for x in range( start, end+1 ):
  divs = allDivs( x )
  if len(divs) == 4 and sum(divs) < minSum:
    minDivs = sorted( divs, reverse = True )
    minSum = sum(divs)

print( minSum, minDivs[1] )

