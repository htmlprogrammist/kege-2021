# А.Н. Носкин

for i in range(2,10000+1):
  a = []
  for d in range(1,i//2+1):
    if i % d == 0:
      a.append(d)
  if i == sum(a):
    print(i,len(a))




