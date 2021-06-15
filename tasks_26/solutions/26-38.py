F = open( '26-j9.txt' )

S, N = map( int, F.readline().split() )

a = []
for i in range(N):
  a.append( int(F.readline()) )

a.sort()

last = 0
count = 0
total = 0
iSmall = -1
iLarge = N
sel = []
while iLarge > iSmall+1:
  while iLarge > iSmall+1:
    iLarge -= 1
    if total + a[iLarge] <= S:
      total += a[iLarge]
      count += 1
      last = a[iLarge]
      sel.append( last )
      #print( sorted(sel) )
      break
  while iLarge >= iSmall+1:
    iSmall += 1
    if total + a[iSmall] <= S:
      total += a[iSmall]
      count += 1
      last = a[iSmall]
      sel.append( last )
      #print( sorted(sel) )
      break

print( count, last )
