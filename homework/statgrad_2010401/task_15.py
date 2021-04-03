"""
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без
остатка на натуральное число m».
Для какого наименьшего натурального числа A формула
ДЕЛ(A, 40) /\ (ДЕЛ(780, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(180, x)))
тождественно истинна, то есть принимает значение 1 при любом
натуральном x?

120
"""


def delenie(m, n):
    return m % n == 0


for A in range(2, 1000):
    for x in range(2, 1000):
        # F = delenie(A, 40) and (delenie(780, x) <= (not delenie(A, x) <= not delenie(180, x)))
        F = delenie(A, 40) and (delenie(780, x) <= (delenie(A, x) or not delenie(180, x)))
        if F:
            print(A)
