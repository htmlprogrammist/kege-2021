"""
№ 604
Определите сумму чисел, которые выведет процедура при вызове F(50).
```
def F(n):
    print(2 * n + 1)
    if n > 1:
        print(3 * n - 8)
        F(n - 1)
        F(n - 4)
```

170480034
"""
summa = 0


def F(n):
    global summa
    summa += 2 * n + 1
    if n > 1:
        summa += 3 * n - 8
        F(n - 1)
        F(n - 4)
    return summa


F(50)
print(summa)
