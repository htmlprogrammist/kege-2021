x = int(input())
L = 0
M = 0
while x > 0:
    L += 1
    if (x % 10) > M:
        M = x % 10
    x = x // 10
    print('X=', x)
print(L)
print(M)
