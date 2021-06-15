start, end = 228224, 531135

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
  divs = allDivs(x)[1:-1]
  cubes = [d for d in divs
               if round(d**(1/3))**3 == d and d % 2 == 1]
  if len(cubes) >= 4:
    print( x, len(cubes), max(cubes) )