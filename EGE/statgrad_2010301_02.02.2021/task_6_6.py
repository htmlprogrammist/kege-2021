# s = int(input())
# s = (s + 1) // 7
# n = 36
# while s < 2050:
#     s *= 2
#     n += 3
# print(n)
for i in range(6, 100):
    s = (i + 1) // 7
    n = 36
    while s < 2050:
        s *= 2
        n += 3
    if n == 60:
        print(i)
        break
