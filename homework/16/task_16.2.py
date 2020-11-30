"""
F(n) = 3, при n = 1
F(n) = 2 * F(n-1) - n + 1, если n > 1
Чему равно значение функции F(21)?
"""


def F(n):
    if n > 1:
        return 2 * F(n-1) - n + 1
    else:
        return 3


print(F(21))  # 1048598
# Совпало с Excel'ем
