# Автор: А.Н. Носкин

﻿with open("24-s1.txt") as F:

  k = 0 # счетчик строк с буквами A*R
  while True:
    s = F.readline() # команда прочитать строку
    if not s: break
    s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in s1:
      stroka = "A"+x+"R"
      if s.count(stroka)>0:
        k +=1
        break # встретилась хоть одна комбинация
  print(k)



