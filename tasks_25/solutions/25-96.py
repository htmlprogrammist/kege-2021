start, end = 81234, 134689

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
  if len(divs) == 5:
    print( divs[1], divs[3] )