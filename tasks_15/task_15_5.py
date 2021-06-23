def d(n, m):
    return n % m == 0


a = []
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not((d(x, A) and d(x, 16)) <= (not(d(x, 16)) or d(x, 24))):
            flag = False
            break
    if flag:
        a.append(A)

print(a)
