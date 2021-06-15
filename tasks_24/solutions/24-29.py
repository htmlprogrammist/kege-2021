# Автор: А.Н. Носкин

# два способа решения:
# - добавлением полного блока букв или по буквенно

with open("k7b-3.txt") as Fin:
  s = Fin.readline()

c = 'BAFE'
while c in s: # ищем BAFE, потом BAFEBAFE  и т.д.
    c += 'BAFE'

if c[:-1] in s: # неполная строка BAFEBAF
  print(len(c)-1)
elif c[:-2] in s: #неполная строка BAFEBA
  print(len(c)-2)
elif c[:-3] in s: #неполная строка BAFEB
  print(len(c)-3)
else:
    print(len(c)-4) # полная строка
  

# 2-й способ
with open("k7b-3.txt") as Fin:
  s = Fin.readline()
c = 'BAFE'
while c in s: # ищем BAFE, потом BAFEB и т.д
    if c[-1]=="B": c +="A"
    elif c[-1]=="A": c +="F"
    elif c[-1]=="F": c +="E"
    elif c[-1]=="E": c +="B"
print(len(c)-1) 












