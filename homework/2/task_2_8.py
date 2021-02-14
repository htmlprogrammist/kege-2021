"""
Задание 2 (№80).
Вася успел заполнить лишь фрагмент таблицы истинности для выражения
F = ((x → y) ∨ ¬ (z → w)) ∧ ((w → ¬x) ∨ (¬y → z)),
даже не указав, какому столбцу таблицы соответствует каждая из переменных w, x, y, z.
"""
print('x y z w F')
r = 0, 1
for x in r:
    for y in r:
        for z in r:
            for w in r:
                # pass
                # F = ((x <= y) or not(z <= w) and ((w <= not x) or (not y <= z)))
                F = (((x <= y) or not(z <= w)) and ((not w or not x) or (not y <= z)))
                if not F:
                    print(x, y, z, w, F)
