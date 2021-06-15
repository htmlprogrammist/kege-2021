start, end = 326496, 649632

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

for x in range( start, end+1 ):
  divs = allDivs(x)
  even = [d for d in divs if d % 2 == 0]
  odd = [d for d in divs if d % 2 == 1]
  if len(odd) == len(even) and len(even) >= 70:
    print( x, min( d for d in divs if d > 1000 ) )