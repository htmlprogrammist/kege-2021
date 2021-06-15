from math import sqrt

start, end = 87921, 88187

def sumprod( x ):
  digits = list(map(int, str(x)))
  prod = 1
  for d in digits:
    prod *= d
  return sum(digits), prod

count = 0
data = []
for x in range( start, end+1 ):
  s, p = sumprod( x )
  if s % 14 == 0 and p != 0 and p % 18 == 0:
    data.append( (s, p) )

data.sort( key = lambda x: x[1] )
for s, p in data:
  print( s, p )