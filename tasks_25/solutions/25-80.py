from math import sqrt

start, end = 2, 10000000

Lim = 100
active = [True]*(Lim + 1)
# Берëм невычеркнутые числа от 2 до sqrt(n)
for i in range(2, round(sqrt(Lim))):
	# Вычëркиваем числа, кратные невычеркнутому
	for j in range(i*i, Lim+1, i):
		active[j] = False
# Все невычеркнутые числа - простые
primes = [i for i in range(2, Lim) if active[i]]

count = 0
product = 1
while product*primes[count] < end:
  product *= primes[count]
  count += 1

#print( product, count )

prev = product // primes[count-1]

iMax = count
while prev*primes[iMax] < end:
  iMax += 1

primes = primes[:iMax+1]

xMaxLen = []
for x in range( start, end+1 ):
  primaryDivs = [ d for d in primes if x % d == 0 ]
  if len(primaryDivs) == count:
    xMaxLen.append(x)

for x in xMaxLen:
  print( x, count )

