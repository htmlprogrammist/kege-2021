s, e = 2000000, 3000000

def valid(x):
  q = round(x**0.5)
  k = 0
  d2Max = 0
  for i in range(70):
    d1 = q - i
    if x % d1 == 0:
      d2 = x // d1
      #print( d1, d2, d2 - d1 )
      if d2 - d1 <= 120:
        k += 1
        d2Max = max(d2, d2Max)
  if k < 3:
    return 0
  else:
    return d2Max

c = 0
for x in range(s, e+1):
  maxDiv = valid(x)
  if maxDiv > 0:
    c += 1
    print( x, maxDiv )
