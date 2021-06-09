s = ''


def F(n):
    global s
    if n > 2:
        F(n // 2)
        F(n - 1)
        # print(n)
        s += str(n)


F(7)
print(s)  # 3334567
