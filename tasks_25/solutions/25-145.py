# Автор: С.О. Куров

k = 0
for i in range(1000000, 1300001):
    if max(set(str(i))) < '3' and sum(map(int, str(i)))%10==0:
        k += 1
        if k%10==0:
            count = 0
            for d in range(2,i):
              if i % d == 0:
                count += 1
            print( i, count )