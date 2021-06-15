start, end = 333555, 777999

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
  digits2 = [ d for d in divs if 10 <= d <= 99 ]
  if len(digits2) == 35:
    print( x, digits2[0], digits2[-1] )