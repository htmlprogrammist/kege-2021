start, end = 394441, 394505

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
for x in range( start, end+1 ):
  divs = allDivs( x )
  if len(divs) > len(maxDivs):
    maxDivs = divs

print( len(maxDivs), maxDivs[-1], maxDivs[-2] )

