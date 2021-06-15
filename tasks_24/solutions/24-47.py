# Автор: А.Н. Носкин

with open("k7-m22.txt") as F:
  s = F.readline() # считали строку

k = 0 # кол-во троек букв
index = -1 # индекс каждой буквы в строке
for i in range(len(s)-2):
  index += 1
  if s[i]> s[i+1]> s[i+2]: # проверка убывания
    k += 1
    r = index # индекс 1й буквы в тройке
    
print(k, r)


  

  



