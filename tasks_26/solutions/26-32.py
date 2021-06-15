from math import ceil
from collections import Counter

with open("26-s1.txt") as F:
  data = F.readlines()

L = 150
D = 0.8

N = int(data[0])
del data[0]
data = data[:N]

data = list(map(int, data))
# print(min(data), max(data))

dataGT_L  = sorted([x for x in data if x > L])
S = sum( x for x in data if x <= L )

nDisc = len(dataGT_L) // 2
dataGT_Ldisc = dataGT_L[:nDisc]
dataGT_L = dataGT_L[nDisc:]
S += sum(dataGT_Ldisc)*D + sum(dataGT_L)

print( ceil(S), dataGT_Ldisc[-1] )
