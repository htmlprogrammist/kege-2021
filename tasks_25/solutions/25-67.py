a, b = 33333, 55555
def isValid( x ):
  return d[0] % 2 != 0 and d[1] % 2 != 0 and d[2] % 2 == 0 and \
         d[3] % 2 != 0 and d[4] % 2 == 0 and \
         x % 6 != 0 and x % 7 != 0 and x % 8 != 0

xMin = 10**10
xMax = 0
count = 0
for x in range(a, b+1):
  d = list( map(int, str(x)) )
  if isValid(x):
    count += 1
    xMin = min( x, xMin )
    xMax = max( x, xMax )

print( count, xMax - xMin )
