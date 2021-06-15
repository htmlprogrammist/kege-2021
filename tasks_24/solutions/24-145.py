# Автор: А.Н. Носкин

with open("24-j7.txt") as F:
  s = F.readline().strip()# читаем строку и удаляем скрытые символы

Max = 0 # макс длина цепочки
s1 = "" # строка из нечетных цифр
s2 = "" # строка из четных цифр
for c in s:
    if int(c)%2 == 0 :
        s1 = ""
        s2 += c
        if len(s2)> Max:
            Max = len(s2) 
    else:
        s2 = ""
        s1 += c
        if len(s1)> Max:
            Max = len(s1) 
print(Max)        
      
    
 







