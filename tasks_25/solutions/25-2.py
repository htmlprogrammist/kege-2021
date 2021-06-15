# А.Н. Носкин

for n in range(102714, 102725+1):
  a = []# массив хранения делителей
  for d in range(1,n+1):
    if n % d == 0:
      a.append(d)
      if len(a) > 4: break
  if len(a) == 4:
    print(*a)


# 2-й спососб
for n in range(102714, 102725+1):
  a = []# массив хранения делителей
  for d in range(1,n//2+1):
    if n % d == 0:
      a.append(d)
      if len(a) > 3: break
  if len(a) == 3:# добавим n
    a.append(n)
    print(*a)

