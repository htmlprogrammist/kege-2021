"""
Р-33.  (С.С. Поляков) Укажите наибольшее целое значение А, при котором выражение
**(y – x != 5) ∨ (A < 2x^3 + y) ∨ (A < y^2 + 16)**
истинно для любых целых положительных значений x и y.
"""
result = []


def F(x, y, A):
    return (y - x != 5) or (A < 2*(x**3) + y) or (A < y**2 + 16)


for A in range(1, 100):
    OK = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not F(x, y, A):
                OK = False
                break
    if OK:
        result.append(A)
print(max(result))

# Перебор А, но в обратную сторону
# for A in range(100, 0, -1):
#     OK = True
#     for k in range(1,1000):
#         for n in range(1,1000):
#             if not f(k, n, A):
#                 OK = False
#                 break
#     if OK:
#         print(A)
#         break
