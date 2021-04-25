"""
292) (Досрочный ЕГЭ-2018)
Укажите наименьшее целое значение А, при котором выражение
(y + 2x < A) ∨ (x > 20) ∨ (y > 40)
истинно для любых целых положительных значений x и y.

"""

A = 1
while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((y + 2*x < A) and (x <= 20) and (y <= 40)):
                break
        else:
            continue
        break
    else:
        print(A)
    A += 1
