def F(x, y, A):
    # return ((6*x + 4*y != 34) or (A > 5*x + 3*y) and (A > 4*y + 15*x - 35))
    return (6 * x + 4 * y != 34) or (A > 5 * x + 3 * y) and (A > 4 * y + 15 * x - 35)


for A in range(1, 100):
    allowance = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not F(x, y, A):
                allowance = False
                break
    if allowance:
        print(A)
        break
