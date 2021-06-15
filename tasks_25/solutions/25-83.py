start, end = 2, 2000

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

def collect( divs, left ):
  if left == 0:
    return True
  if left < 0:
    return False
  if not divs:
    return False
  return collect( divs[1:], left-divs[0] ) or collect( divs[1:], left )

count = 0
sel = []
for x in range( start, end+1 ):
  divs = allDivs(x)[:-1]
  if sum(divs) >= x:
    if collect( divs, x ):
      count += 1
      sel.append( x )

print(count)

