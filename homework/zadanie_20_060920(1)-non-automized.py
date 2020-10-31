x = int(input())
a = 9
d = x
s = 0
while d // 2 > 0:
    if d % 2 == 1:
        s += 1
    else:
        s += a
    d = d // 2
print(s)
