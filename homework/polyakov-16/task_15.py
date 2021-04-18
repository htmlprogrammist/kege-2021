"""
(№ 2245) Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
Для какого наибольшего натурального числа A формула
¬ДЕЛ(x, 18) → (¬ДЕЛ(x, A) → ¬ДЕЛ(x, 12))
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?

12
"""
answers = []


def delenie(m, n):
    return m % n == 0


for A in range(1, 100):
    for x in range(1, 1000):
        # F = not delenie(x, 18) <= (delenie(x, A) or not delenie(x, 12))
        F = delenie(x, 18) or delenie(x, A) or not(delenie(x, 12))
        if F:
            answers.append(A)

set(answers)
print(min(answers))
