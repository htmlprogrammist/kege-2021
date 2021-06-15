start, end = 100000000, 300000000

from math import log

max2deg = int( log(end/7)/log(2) )
max2deg -= max2deg % 2
d2 = 2**max2deg
deg2 = max2deg
result = []
while d2 > 0:
  deg7, d7 = 1, 7
  while d2*d7 <= end:
    if start <= d2*d7:
      result.append( (d2*d7, deg2, deg7) )
    d7 *= 7**2
    deg7 += 2
  d2 //= 2**2
  deg2 -= 2

for x, d2, d7 in  sorted(result):
  print( x, d2+d7, d2, d7 )