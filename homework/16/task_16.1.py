"""
F(n) = 1, при n = 1
F(n) = 2 * F(n-1) + n + 3, если n > 1
Чему равно значение функции F(19)?
"""


def F(n):
    if n > 1:
        return 2 * F(n - 1) + n + 3
    else:
        return 1


print(F(19))  # 1834984
# Совпало с Excel'ем
