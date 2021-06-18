"""
Задание 2 (№1422).
¬(z ∧ ¬w) ∨ ((z → w) ≡ (x → y))
"""
print('x y z w F')
k = 0, 1
for x in k:
    for y in k:
        for z in k:
            for w in k:
                F = not(z and not(w)) or ((z <= w) == (x <= y))
                if not F:
                    print(x, y, z, w, F)
