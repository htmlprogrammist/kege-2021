start, end = 135790, 163228

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
  s = sum(divs)
  if s > 460000:
    print( len(divs), s )