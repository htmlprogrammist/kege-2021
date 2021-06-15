# Автор: А.Н. Носкин

with open("26-j8.txt") as F:
  n = int(F.readline()) # 1я строка файла

  # n -  кол-во товаров
  a = [] # массив хранения всех цен
  """ ввод всех цен из файла"""
  for i in range(n):
    stroka = F.readline()  # прочитали очередную цену в виде строки
    a.append(int(stroka)) #  цену добавили в массив в виде числа

  a.sort() # сортировка цен по возрастанию
  """ 1я акция: расчет цены при скидке 30% и 40%"""
  summa = 0 # сумма цен
  n = int(len(a)*0.7) # кол-во 70% товаров
  for i in range(n): 
        summa += a[i]*0.7 # цена со скидкой 30%
  for i in range(n,len(a)): 
        summa += a[i]*0.6 # цена со скидкой 40%

  """ 2я акция: расчет цены при скидке 40% и 35%"""
  summa2 = 0 # сумма цен
  n = int(len(a)*0.5) # кол-во 50% товаров
  for i in range(n): 
        summa2 += a[i]*0.6 # цена со скидкой 40%
  for i in range(n,len(a)): 
        summa2 += a[i]*0.65 # цена со скидкой 35%     
  pazn = int(abs(summa - summa2))# разность прибылей
  if summa2 > summa: a[-1] *= 0.65
  else: a[-1] *= 0.6
  print(pazn,int(a[-1]))
