# А.Н. Носкин

k=0 # порядковый номер

for i in range(2532000, 2532160+1):
    count = 2 # есть  1 и само число
    for j in range(2,round(i**0.5)+1): 
        if i%j == 0:
            count = 0 
            break # не простое 
    if count == 2 and i%10 == 7:
        k +=1
        print(k,i)

