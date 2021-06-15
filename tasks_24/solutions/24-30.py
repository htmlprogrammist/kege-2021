# Автор: А.Н. Носкин

# два способа решения:
# - добавлением полного блока букв или по буквенно

with open("k7b-4.txt") as Fin:
  s = Fin.readline()

c = 'EBCF'
while c in s: # ищем EBCF, потом EBCFEBCF и т.д.
    c += 'EBCF'

if c[:-1] in s: print(len(c)-1) # неполный блок EBCFEBC
elif c[:-2] in s: print(len(c)-2) # неполный блок EBCFEB
elif c[:-3] in s: print(len(c)-3) # неполный блок EBCFE
else: print(len(c)-12) # полный блок EBCF
  
# 2-й способ
with open("k7b-4.txt") as Fin:
  s = Fin.readline()
c = 'EBCF'
while c in s: # ищем EBCF, потом EBCFE и т.д
    if c[-1]=="E": c +="B"
    elif c[-1]=="B": c +="C"
    elif c[-1]=="C": c +="F"
    elif c[-1]=="F": c +="E"
print(len(c)-1) 













