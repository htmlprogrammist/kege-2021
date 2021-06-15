start, end = 394480, 394540

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

maxDivs = []
maxLen = 0
for x in range( start, end+1 ):
  divs = allDivs( x )
  if len(divs) >= maxLen:
    if len(divs) > maxLen:
      maxDivs = []
    maxDivs.append( divs )
    maxLen = len(divs)

for i, divs in enumerate(maxDivs):
  print( i+1, len(divs), divs[-1], divs[-2] )


