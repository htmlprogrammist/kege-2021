"""
Логическая функция 𝐹 задаётся выражением:
((¬𝑥 \/ 𝑧) ≡ (𝑦 /\ ¬𝑤)) → (𝑧 /\ 𝑦).
F = 0
"""
print('x y z w F')
k = 0, 1
for x in k:
    for y in k:
        for z in k:
            for w in k:
                F = ((not x or z) == (y and not w) <= (z and y))
                if not F:
                    print(x, y, z, w, F)
