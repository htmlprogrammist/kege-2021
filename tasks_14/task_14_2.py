"""
№ 243
Определите число N, для которого выполняется равенство 132|N + 13|8 - 124|N+1 = 0.
| - значит в основание

6
"""

for n in range(2, 10):
    try:
        if int('132', n) + int('13', 8) - int('124', n + 1) == 0:
            print(n)
            break
    except ValueError:
        pass
