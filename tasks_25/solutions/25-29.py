from math import sqrt

start, end = 652938, 1744328

qStart = int(sqrt(start))
qEnd = int(sqrt(end))+1
for q in range( qStart, qEnd+1 ):
  n = q*q
  a = [q] # массив для хранения делителей
  for d in range(1, q):
    if n % d == 0:
      a = a + [d, n//d]
      if len(a) > 5: break
  if len(a) == 5:
    print( *sorted(a) )
