start, end = 150000000, 300000000

from math import log

max2deg = int( log(end/3)/log(2) )
max2deg -= max2deg % 2
d2 = 2**max2deg
deg2 = max2deg
result = []
while d2 > 0:
  deg3, d3 = 1, 3
  while d2*d3 <= end:
    if start <= d2*d3:
      result.append( (d2*d3, deg2, deg3) )
    d3 *= 3**2
    deg3 += 2
  d2 //= 2**2
  deg2 -= 2

for x, d2, d3 in  sorted(result):
  print( x, d2+d3 )