from math import sqrt

start, end = 3594, 21891

def countDivs( x ):
  count = 2
  q = round(sqrt(x))
  if q*q == x:
    return 0
  for d in range(2, q+1):
    if x % d == 0:
      count += 2
  return count

for x in range( end, start-1, -1 ):
  if countDivs(x) == 4:
    print(x)
    break
