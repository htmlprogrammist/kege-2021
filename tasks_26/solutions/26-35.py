with open("26-j7.txt") as F:
  n = int(F.readline())
  data = []
  for i in range(n):
    data.append( int(F.readline()) )

data.sort( reverse = True )

S = sum(data)*0.6

rich = int(0.2*n) # или n // 5
richSum = 0.8*sum( data[:rich] )

restSum = S - richSum
percent = restSum / sum(data[rich:])

print( int(richSum), int(percent*data[-1]) )




