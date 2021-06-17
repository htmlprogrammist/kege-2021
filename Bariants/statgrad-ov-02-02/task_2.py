"""
(x → y) /\ (x \/ not z) /\ (x ≡ not w)
"""
print('x y z w F')
k = 0, 1
for x in k:
    for y in k:
        for z in k:
            for w in k:
                F = (x <= y) and (x or not(z)) and (x != w)
                if F:
                    print(x, y, z, w, F)
