# Автор В.Н. Шубинкин
'''
Идея решения. Создадим двумерный список простых чисел,
в котором под индексом i соберём простые числа,
оканчивающиеся на цифру i.
Затем переберём тройки простых чисел, заканчивающихся одинаковой цифрой
и добавим в списко ans те из них,
произведение которых лежит в требуемом диапазоне.
'''
start, end = 416782, 498324

# генерация списка простых чисел
primes = [ [] for i in range(10) ]
for i in range(2, end//3//13):
    for d in range(2, int(i ** 0.5) + 1):
        if i % d == 0:
            break
    else:
        primes[i % 10].append(i)

ans = []
# перебор возможных троек
for ind in range(1, 10, 2):
    for i in range(len(primes[ind])):
        if primes[ind][i] > end**(1/3):
            break
        for j in range(i + 1, len(primes[ind])):
            if primes[ind][i] * primes[ind][j] > end**(2/3):
                break
            for k in range(j + 1, len(primes[ind])):
                p = primes[ind][i] * primes[ind][j] * primes[ind][k]
                if p > end:
                    break
                if p in range(start, end+1):
                    ans.append(p)

print(len(ans), max(ans) - min(ans))
