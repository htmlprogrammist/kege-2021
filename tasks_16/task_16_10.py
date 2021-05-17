"""
64
"""
from functools import *


@lru_cache(None)
def f(n):
    if n <= 3:
        return n
    if n > 3:
        if n % 2 == 0:
            return f(n - 1) + 2 * f(n // 2)
        else:
            return f(n - 1) + f(n-3)


counter = 0
for n in range(1, 67890):
    result = f(n)
    if result < 10 ** 8:
        counter += 1

print(counter)
