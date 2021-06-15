# А.Н. Носкин

for n in range(190061,190080+1):
  a = []
  for d in range(1,n+1):
    if n % d == 0 and d%2!=0:
      a.append(d)
      if len(a) > 4: break
  if len(a) == 4:
      a.reverse()
      print(*a)




