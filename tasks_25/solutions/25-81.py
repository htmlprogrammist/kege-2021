start, end = 2, 263000

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
  sDivs = sum(allDivs( x ))
  if sum(allDivs(sDivs)) == 2*x:
    print( x )
