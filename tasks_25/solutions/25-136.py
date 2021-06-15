# А.Н. Носкин

a = [] 
for i in range(2,1000+1):
    count = 2 
    for j in range(2,round(i**0.5)+1): 
        if i%j == 0:
            count = 0 
            break 
    if count == 2:
        a.append(i)

""" ищем 6 делителей"""
for i in range(25317, 51237+1):
    k = 0 
    for j in range(len(a)): 
        if i%a[j] == 0:
            k += 1 
        if k >= 6:
            print(i, a[j])
            break


