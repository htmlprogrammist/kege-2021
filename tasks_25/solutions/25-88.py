from math import sqrt

start, end = 2031, 14312

def valid( x ):
  while x:
    if x % 11 == 2:
      return False
    x //= 11
  return True

for x in range( start, end+1 ):
  if valid(x):
    xMax = x

print( xMax )