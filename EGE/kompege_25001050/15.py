"""
Задание 15 (№880).
Обозначим через ДЕЛ(n, m) утверждение
«натуральное число n делится без остатка на натуральное число m».
Для какого наибольшего натурального числа A формула
ДЕЛ(70, A) ∧ (¬ДЕЛ(x, A) → (ДЕЛ(x, 18) → ¬ДЕЛ(x, 42)))
тождественно истинна, то есть принимает значение 1 при любом натуральном х?
"""


def deletion(m, n):
    return m % n == 0


# def f(A, x):
#     return deletion(70, A) and (not deletion(x, A) <= (deletion(x, 18) <= not(deletion(x, 42))))


for A in range(1, 100):
    OK = True
    for x in range(1, 1000):
        if not f(A, x):
            OK = False
    if OK:
        mx = A
print(mx)
