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

start = 700000
prevNDivs = len(allDivs(start))
print( start, prevNDivs )
count = 1
x = start + 1
while count < 5:
  nDivs = len(allDivs(x))
  if nDivs > prevNDivs:
    prevNDivs = nDivs
    print( x, nDivs )
    count += 1
  x +=1
