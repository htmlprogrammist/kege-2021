def firstPrimes( n ):
  primes = [2]
  k = 3
  while len(primes) < n:
    divs = [int(k % d == 0)  for d in primes]
    if sum(divs) == 0:
      primes.append( k )
    k += 1
  return primes

def factorize(x):
  primeDels = []
  k = 2
  while x > 1:
    while x % k == 0:
      primeDels.append(k)
      x /= k
    k += 1
  return primeDels

primeFactors = factorize(512)
primeFactors.reverse()
primes = firstPrimes(len(primeFactors))
N = 1
for i in range(len(primeFactors)):
  N *= primes[i]**(primeFactors[i]-1)

k2 = primeFactors[0]
lastPrime = primes[-1]
while 2**k2 < lastPrime:
  N = N // lastPrime * 2**k2
  k2 *= 2
  del primes[-1]
  lastPrime = primes[-1]

if N < 2**31:
  print( N, primes[-1] )
else:
  print('NO')



