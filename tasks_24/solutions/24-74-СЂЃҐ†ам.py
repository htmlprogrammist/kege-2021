# Автор: А.Н. Носкин

with open("k8-6.txt") as F:
  s = F.readline() # считали строку

d = {} # массив хранения всех цепочек
stroka = s[0] # первый символ строки
k = 1
for i in range(len(s)-1):
  if s[i] == s[i+1]: # сравнение соседних символов
    stroka += s[i+1] # формирование строки = ключа
    
  else:
    if stroka not in d: # проверка отсутствия ключа в словаре
      d[stroka] = len(stroka) # ключ (строка) : значение (длина)
    else:
      Len = len(stroka)
      k +=1
      stroka += str(k)
      d[stroka] = Len # ключ (строка) : значение (длина)

    stroka = s[i+1] # новая цепочка для расчетов

if s[-1]==s[-2]: # проверка окончании строки на одни символы
  if stroka not in d: # проверка отсутствия ключа в словаре
      d[stroka] = len(stroka) # ключ (строка) : значение (длина)
  else:
      Len = len(stroka)
      k +=1
      stroka += str(k)
      d[stroka] = Len # ключ (строка) : значение (длина)
  
Max = max(d.values())# максимальное значание ключа
a = [x[0] for x in d.items() if x[1]==Max] # массив ключей
for x in a:
  print(x[0],Max) # первая буква ключа и значение



 




