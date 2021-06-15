# Автор: А.Н. Носкин

with open("26-k1.txt") as F:
  nC, n = map(int, F.readline().split()) # 1ю строку файла в 2 числа
# nC  - количество цен
# n -  кол-во товаров со скидкой

  a = [] # массив хранения всех цен
  """ ввод всех цен из файла"""
  for i in range(nC):
    stroka = F.readline()  # читаем очередную цену (строку)
    a.append(int(stroka)) #  цену добавили в массив

  a.sort(reverse = True) # сортировка цен по убыванию 

  """ расчет суммы скидок 20%"""
  summa = 0 # сумма скидок
  for i in range(n): 
        summa += a[i]*0.2
  print(a[n],int(summa)) # целая часть от суммы

