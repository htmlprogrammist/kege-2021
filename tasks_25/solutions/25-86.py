from math import sqrt

start, end = 4986, 32599

def countDivs( x ):
  count = 2
  q = round(sqrt(x))
  if q*q == x:
    return 0
  for d in range(2, q+1):
    if x % d == 0:
      count += 2
  return count

s = 0
for x in range( start, end+1 ):
  nDivs = countDivs(x)
  if nDivs == 4:
    s += x

print( s )