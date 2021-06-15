# Автор: А.Н. Носкин

﻿with open( "k8-8.txt" ) as F:
  s = F.readline()

Max = 0 #макс длина цепочки разных символов
k = 1 #длина текущей цепочки разных символов 
for i in range(len(s)-1):
  if s[i] != s[i+1]:
    k += 1
    if k > Max:
      Max = k
  else:
    k = 1 # появилась новая цепочка
print(Max)


