s, e = 834567, 1143210

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

def valid( divs ):
  if len(divs) < 2: return False
  for i in range(1, len(divs)):
    if divs[i] - divs[i-1] != 2:
      return False
  return True

for x in range(s, e+1):
  divs = allDivs(x)[1:-1]
  if valid(divs):
    print( x, divs[-1] )

