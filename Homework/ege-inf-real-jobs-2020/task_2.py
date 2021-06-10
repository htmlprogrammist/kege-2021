"""
(x /\ ¬y) \/ (x ≡ z) \/ w
"""
print('x y z w F')
k = 0, 1
for x in k:
    for y in k:
        for z in k:
            for w in k:
                F = (x and not y) or (x == z) or w
                if not F:
                    print(x, y, z, w, F)
