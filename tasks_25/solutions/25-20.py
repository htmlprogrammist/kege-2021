start, end = 100806, 100950

for n in range( start, end+1 ):
  a = [] # массив для хранения делителей
  for d in range(1,n+1):
    if n % d == 0:
      a.append(d)
      if len(a) > 6: break
  if len(a) == 6:
    print( *a )
