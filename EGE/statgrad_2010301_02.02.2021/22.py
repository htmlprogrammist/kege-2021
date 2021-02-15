# x = int(input())
# m = 0
# s = 0
# while x > 0:
#     d = x % 8
#     s += d
#     if d > m:
#         m = d
#     x //= 8
# print(m, s)

answer_m = 5
answer_s = 12
number = 0
while number < 100:
    x = number
    m = 0
    s = 0
    while x > 0:
        d = x % 8
        s += d
        if d > m:
            m = d
        x //= 8
    if s == answer_s and m == answer_m:
        print(number)
        break
