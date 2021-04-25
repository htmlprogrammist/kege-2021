A = 1
while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not (((4 * x + 3 * y) < A) or (x >= y) or (y >= 13)):
                break
        else:
            continue
        break
    else:
        print(A)
    A += 1
