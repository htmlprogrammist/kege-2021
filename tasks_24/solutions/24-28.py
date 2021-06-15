# Автор: А.Н. Носкин

# два способа решения:
# - добавлением полного блока букв или по буквенно

with open("k7b-2.txt") as Fin:
  s = Fin.readline()

c = 'DBAC'
while c in s:  # ищем DBAC, потом DBACDBAC  и т.д.
    c += 'DBAC'

if c[:-1] in s: # неполная строка DBACDBA
  print(len(c)-1)
elif c[:-2] in s: #неполная строка DBACDB
  print(len(c)-2)
elif c[:-3] in s: #неполная строка DBACD
  print(len(c)-3)
else:
    print(len(c)-4) # полная строка

# 2-й способ
with open("k7b-2.txt") as Fin:
  s = Fin.readline()
c = 'DBAC'
while c in s: # ищем DBAC, потом DBACD и т.д
    if c[-1]=="D": c +="B"
    elif c[-1]=="B": c +="A"
    elif c[-1]=="A": c +="C"
    elif c[-1]=="C": c +="D"
print(len(c)-1) 



  














