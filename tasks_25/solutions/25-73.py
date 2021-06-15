# А.Н. Носкин

k = 0

for i in range(2,20000+1):
  a = []
  for d in range(1,i//2+1):
    if i % d == 0:
      a.append(d)
  if i < sum(a):
    k +=1

print(k)




