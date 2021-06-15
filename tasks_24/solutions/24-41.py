# Автор: А.Н. Носкин

with open("k7-m3.txt") as F:
  s = F.readline() # считали строку

a = [] # массив хранения всех цепочек "С"
s_C = ""
for c in s:
  if c == 'C': # накапливание "С"
    s_C += 'C'
  else:
    if s_C != '': # добавили в массив, когда другая буква
      a.append(s_C)
    s_C = "" # новая цепочка для расчетов

if s[-1]=="C": a.append(s_C)
k = 0
for x in a:
  if len(x)<5:
    k+=1
    print(k,len(x),(x[0]+(len(x)-1)*"c"))
  

  



