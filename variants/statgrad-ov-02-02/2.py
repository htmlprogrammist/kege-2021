"""
Логическая функция F задаётся выражением:
((x ≡ ¬y) → (y /\ ¬z)) \/ (z /\ ¬w).
Дан частично заполненный фрагмент, содержащий неповторяющиеся
строки таблицы истинности функции F.
Определите, какому столбцу таблицы истинности соответствует каждая
из переменных w, x, y, z.
"""
print('x y z w F')
r = 0, 1
for x in r:
    for y in r:
        for z in r:
            for w in r:
                # F = ((x == not y) <= (y and not z) or (z and not w))
                F = ((not y == x) <= (y and not z) or (z and not w))
                # F = (not ((x == not y) and not (y and not z)) or (z and not w))
                if not F:
                    print(x, y, z, w, F)
