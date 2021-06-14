"""
Задание 2 (№1422).
Миша заполнял таблицу истинности логического выражения
¬(z ∧ ¬w) ∨ ((z → w) ≡ (x → y))
но успел заполнить лишь фрагмент и трёх различных её строк, даже не указав,
какому столбцу таблицы соответствует каждая из переменных w, x, y, z
Определите, какому столбцу таблицы соответствует каждая из переменных w, x, y, z
В ответе запишите буквы w, x, y, z в том порядке, в котором идут соответствующие столбцы.
"""
print("x y z w F")
k = 0, 1
for x in k:
    for y in k:
        for w in k:
            for z in k:
                F = not(z and not(w)) or ((z <= w) == (x <= y))
                if not F:
                    print(x, y, z, w, F)
