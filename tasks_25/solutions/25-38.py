from math import sqrt

start, end = 268220, 270335

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
maxSum = 0
maxDivs = []
for x in range( start, end+1 ):
  divs = allDivs( x )
  if len(divs) <= 4 and sum(divs) > maxSum:
    maxDivs = sorted( divs, reverse = True )
    maxSum = sum(divs)

print( maxSum, len(maxDivs), *maxDivs )

