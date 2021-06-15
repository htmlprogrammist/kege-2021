from math import sqrt

start, end = 1000, 20000

for i in range( start, end+1 ):
  q = round(sqrt(i))
  if q*q == i:
    a = [1, q]
  else:
    a = [1]
    q += 1
  for d in range(2,q):
    if i % d == 0:
      a = a + [d, i//d]
  if i == sum(a)+1:
    print( i )

