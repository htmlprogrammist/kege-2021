def Del(x, D):
    return x % D == 0


def F(x, A):
    return Del(x, A) <= ((not Del(x, 28)) or (Del(x, 42)))


for A in range(1, 1000):
    OK = True
    for x in range(1, 1000):
        if not F(x, A):
            OK = False
            break
    if OK:
        print(A)
        break
