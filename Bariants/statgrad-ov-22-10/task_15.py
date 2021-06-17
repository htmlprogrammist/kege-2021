"""
Обозначим через ДЕЛ(n, m) утверждение "натуральное число n делится без остатка на натуральное число m".
Для какого наибольшего натурального числа A формула
(A < 50) /\ (not ДЕЛ(x, A) → (ДЕЛ(x, 10) → not ДЕЛ(x, 12)))
тождественно истинна, т. е. принимает значение 1 при любом натуральном x?
"""
a = []


def dele(n, m):
    return n % m == 0


for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        # if ((A < 50) and (not(dele(x, A)) <= (dele(x, 10)) <= not(dele(x, 12))))
        if not( (A < 50) and (dele(x, A) or not( dele(x, 10) and (dele(x, 12)) )) ):
            flag = False
            break
    if flag:
        a.append(A)
print('Ответ:', max(a), ';', a)
