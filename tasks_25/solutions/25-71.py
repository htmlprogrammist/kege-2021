# А.Н. Носкин

""" массив простых чисел до 1000"""
a = [] # массив простых чисел
for i in range(2, 1000+1):
    count = 2 # есть  1 и само число
    for j in range(2,round(i**0.5)+1): 
        if i%j == 0:
            count = 0 
            break # не простое 
    if count == 2:
        a.append(i)
""" Проверяем деление каждого
числа на простое. Ищем > 3х"""

count = 0 

for i in range(2, 20000+1):
    k = 0
    for j in range(len(a)): 
        if i%a[j] == 0:
            k += 1
        if k > 3:
            count += 1
            break
print(count)
