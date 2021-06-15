
with open("26-k6.txt") as F:
  data = F.readlines()

N, K = map(int, data[0].split())

del data[0]
data = data[:N]

pairs = []
for i in range(N):
  pairs.append( tuple( map(int, data[i].split()) ) )

pairs.sort( key = lambda x: (x[1]/x[0], -x[1]) )

selected = pairs[:K]
print( sum( x[0] for x in selected ), end=" " )
weight = [x[0] for x in selected]
ind = weight.index( max(weight) )
print( selected[ind][1] )


