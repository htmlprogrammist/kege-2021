end_of_interval = 200
x = 100
answer = 49
while x <= end_of_interval:
    # x = int(input())
    a = 8
    d = x
    s = 0
    while d // 2 > 0:
        if d % 2 == 1:
            s += 1
        else:
            s += a
        d = d // 2
    if s == answer:
        print('Answer:', x)
    x += 1
