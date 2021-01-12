"""
---
Р-20 (М.В. Кузнецова).
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка
на натуральное число m». Для какого наименьшего натурального числа А формула
ДЕЛ(x, А) → ((ДЕЛ(x, 21) + ДЕЛ(x, 35))
тождественно истинна
(то есть принимает значение 1 при любом натуральном значении переменной х)?

*Ответ: 21*
"""


def division(m, n):
    return m % n == 0


def f(x, A):
    # return division(x, A) <= (division(x, 21) or division(x, 35))
    return division(x, A) <= (division(x, 21) or division(x, 35))


for A in range(1, 100):
    let = True
    for x in range(1, 1000):
        if not f(x, A):
            let = False
    if let:
        print(A)
        break
