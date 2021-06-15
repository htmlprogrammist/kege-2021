start = 700000

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

prevCount = len(allDivs(start))
numList = [(start, prevCount)]
x = start+1
while True:
  nDivs = len(allDivs(x))
  if nDivs > prevCount:
    numList.append( (x, nDivs) )
    if len(numList) >= 5: break
  else:
    numList = [ (x, nDivs) ]
  prevCount = nDivs
  x +=1

for p in numList:
  print( *p )