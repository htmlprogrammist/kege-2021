with open("26-j10.txt") as F:
  sizeD, sizeE, n = map( int, F.readline().split() )

  large = []
  small = []
  for i in range(n):
    v = int(F.readline())
    if v > 500:
      large.append( v )
    else:
      small.append( v )

large = sorted( large )
cntLarge = 0
sumLarge = 0
while sumLarge + large[cntLarge] <= sizeD:
  sumLarge += large[cntLarge]
  cntLarge += 1

lastLarge = cntLarge
while lastLarge < len(large) and \
      sumLarge - large[cntLarge-1] + large[lastLarge] <= sizeD:
  lastLarge += 1

small = sorted( small )
cntSmall = 0
sumSmall = 0
while sumSmall + small[cntSmall] <= sizeE:
  sumSmall += small[cntSmall]
  cntSmall += 1

lastSmall = cntSmall
while lastSmall < len(small) and \
      sumSmall - small[cntSmall-1] + small[lastSmall] <= sizeE:
  lastSmall += 1

print( cntLarge + cntSmall,
       large[lastLarge-1] + small[lastSmall-1] )







