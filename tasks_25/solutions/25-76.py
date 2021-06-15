from math import sqrt

start, end = 2, 30000

def sumDivs( x ):
  q = round(sqrt(x))
  if q*q == x:
    divs = [1, q]
  else:
    divs = [1]
    q += 1
  for d in range(2,q):
    if x % d == 0:
      divs = divs + [d, x//d]
  return sum(divs)

for i in range( start, end+1 ):
  pair = sumDivs(i)
  if i < pair and i == sumDivs(pair):
    print( i, pair )

