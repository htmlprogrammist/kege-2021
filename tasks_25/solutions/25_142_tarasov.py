# А.Г. Тарасов
# Идея - все элементы искомой последовательности простые числа

import math

def prost(z):                       # проверка числа на простоту 
    for j in range(2,int(math.sqrt(z))+1):
        if z%j == 0: return False
    return True

d=100
b,e = 862346, 1056242

alen=int(math.sqrt(e))+1            # длина массива     
a=[prost(x) for x in range(alen)]   # 

for i in range(2,alen-d):
    f = False
    if a[i]:                        #  если число простое
        k,s=i,i                     # к - число мпоследов-ти s -сумма 
        while k+d<=alen and a[k+d]:
            s*=k+d
            k+=d
            f = True                # в последов-ти более 1 элмем-та
    if f and s>=b:
        print(s,k)                  # если послед. входит в дипазон






