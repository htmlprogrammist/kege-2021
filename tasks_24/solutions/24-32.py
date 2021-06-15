# Автор: А.Н. Носкин

# два способа решения:
# - добавлением полного блока букв или по буквенно

with open("k7b-6.txt") as Fin:
  s = Fin.readline()

c = 'DAF'
while c in s: 
    c += 'DAF'

if c[:-1] in s: # не полная строка DAFDA
  print(len(c)-1)
elif c[:-2] in s: # не полная строка DAFD
  print(len(c)-2)
else:
    print(len(c)-3) 

# 2-й способ
with open("k7b-6.txt") as Fin:
  s = Fin.readline()
c = 'DAF'
while c in s: # ищем DAF, потом DAFD и т.д
    if c[-1]=="D": c +="A"
    elif c[-1]=="A": c +="F"
    elif c[-1]=="F": c +="D"
print(len(c)-1) 














