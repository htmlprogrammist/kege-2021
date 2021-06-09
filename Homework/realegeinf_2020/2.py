print('x y z w F')
k = 0, 1
for x in k:
    for y in k:
        for w in k:
            for z in k:
                F = (x or y) and (y != z) and not(w)
                if F:
                    print(x, y, z, w, F)
