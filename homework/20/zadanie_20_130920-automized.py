end_of_interval = 200
x = 1
answer = 125
while x <= end_of_interval:
    # x = int(input())
    L = 17
    M = 70
    while L <= M:
        L = L + 2*x
        M = M + x
        if L == answer:
            print(x)
    x += 1
