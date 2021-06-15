from math import sqrt

start, end = 1395, 22717

def valid(x):
  prev = 0
  for c in str(x):
    if int(c) < prev:
      return False
    prev = int(c)
  return True

s = 0
for x in range( start, end+1 ):
  if valid(x):
    s += x

print(s)
