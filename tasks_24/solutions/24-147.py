# Автор: А.Н. Носкин

with open("24-s2.txt") as F:
  s = F.readline() # считали строку

d={} # словарь букв
while "A" in s:
  n = s.find("A")# индекс "А"
  key = s[n+1] # создаем ключ = Букве
  d[key] = d.get(key,0)+1
  s = s[n+1:]# срез, формируем новую строку

Max = max(d.values())# макс значение ключа
a = [x[0] for x in d.items() if x[1] == Max]
a.sort()
print(a[0]+str(Max))




