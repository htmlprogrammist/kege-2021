# F(6)
def F(n):
    if n > 2:
        return F(n-1) + F(n-2)
    else: return n
