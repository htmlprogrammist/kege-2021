# L и М, сначала 4, потом 8

# x = int(input())
# Q = 7
# L = 0
# while L < x:
#     L = L + Q
#
# L = Q - L + x
# if L == Q:
#     L = 0
# M = (x - L)
#
# if M < L:
#     M, L = L, M
#
# print(L)
# print(M)

x = 0
answers = []
answer_L = 4
answer_M = 8
# while x < 10000:
while x < 200:
    number = x
    L = 0
    Q = 7
    while L < number:
        L = L + Q

    L = Q - L + number
    if L == Q:
        L = 0
    M = (number - L) // Q

    if M < L:
        M, L = L, M
    if L == answer_L and M == answer_M:
        answers.append(x)
    x += 1
print(answers)
print(max(answers))
