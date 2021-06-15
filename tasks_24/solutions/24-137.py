# Автор: А.Н. Носкин

with open("24-s1.txt") as F:

  k = 0 # счетчик строк 
  while True:
    s = F.readline() # прочитать строку
    if not s: break
    if s.count("J") > s.count("E"):
       k +=1
  print(k)




