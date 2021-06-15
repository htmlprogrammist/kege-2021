with open('26-51.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    data.append( int(F.readline()) )
  #data = [int(s) for s in F]

data.sort()

shift = 100
Q = data[:shift]    # инициализация очереди
data = data[shift:]

count, ma = [0, 0],  [0, 0]
pairs = 0
s = 0
for i in range(len(data)):
     # образуем пары с data[i]
  d = data[i] % 2
  pairs += count[d]
  s = max( s, data[i]+ma[d] )
     # выбираем следующий элемент из очереди
  x = Q.pop(0)
  Q.append( data[i] )
  d = x % 2
  count[d] += 1
  ma[d] = max( ma[d], x )
  # print( x, '->', count, ma, pairs, s )

#print( count, ma )
print( pairs, s//2 )
