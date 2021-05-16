def P(m, n):
    return m & n == 0


def F(x, A):
    return ((P(x, 73)) <= ((not (P(x, 28))) <= (not (P(x, A)))))


for A in range(1, 100):
    f = True
    for x in range(1, 100):
        if not (F(x, A)):
            f = False
            break
    if f:
        print(A)
