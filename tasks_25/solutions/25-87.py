from math import sqrt

start, end = 2945, 18294

def valid( x ):
  count = 2
  while count*count <= x:
    if x % (count*count) == 0:
      return False
    count += 1
  return True

s = 0
for x in range( start, end+1 ):
  if valid(x):
    s += sum( map(int, str(x)) )

print( s )