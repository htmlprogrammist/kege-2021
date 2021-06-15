from math import sqrt

start, end = 1686, 13276

def valid(x):
  noDig = "02468"
  for c in str(x):
    if c in noDig:
      return False
  return True

s = 0
for x in range( start, end+1 ):
  if valid(x):
    s += sum( map(int, str(x)) )

print(s)
