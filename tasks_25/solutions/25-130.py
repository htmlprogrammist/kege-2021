start, end = 50034679, 92136895

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

q4s = int(start**0.25)
q4e = int(end**0.25) + 1
for q4 in range(q4s, q4e+1):
  x = q4**4
  if start <= x <= end  and  isPrime(q4):
    print( x, [q4, q4**2, q4**3] )

