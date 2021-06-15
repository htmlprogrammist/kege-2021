# Автор: А.Н. Носкин

# два способа решения:
# - добавлением полного блока букв или по буквенно

with open("k7b-5.txt") as Fin:
  s = Fin.readline()

c = 'CA'
while c in s: # ищем CA, потом CACA и т.д
    c += 'CA'

if c[:-1] in s:      #неполная цепочка CAC
    print(len(c)-1) 
else: # полная цепочка СА
    print(len(c)-2) 



# 2-й способ
with open("k7b-5.txt") as Fin:
  s = Fin.readline()

c = 'CA'
while c in s: # ищем CA, потом CAC и т.д
    if c[-1]=="C": c +="A"
    elif c[-1]=="A": c +="C"
    
print(len(c)-1) 


















