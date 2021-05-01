"""
F(n) = 2, при n = 1
F(n) = F(n-1) + 5n^2, если n > 1
Чему равно значение функции F(39)?
"""


def F(n):
    if n > 1:
        return F(n-1) + 5 * n**2
    else:
        return 2


print(F(39))  # 102697
# Совпало с Excel'ем
