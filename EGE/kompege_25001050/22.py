"""
Сначала 5, потом 12. Сколько существует трёхзначных X?
"""

# x = int(input())
# a = 0
# b = 1
# while x > 0:
#     if x % 2 > 0:
#         a += x % 11
#     else:
#         b *= x % 11
#     x //= 11
# print(a)
# print(b)
# print('---')

x = 100
answers = []
answer_a = 5
answer_b = 12
while x < 1000:
    number = x
    a = 0
    b = 1
    while number > 0:
        if number % 2 > 0:
            a += number % 11
        else:
            b *= number % 11
        number //= 11
    if answer_a == a and answer_b == b:
        answers.append(x)
    x += 1

print(answers)
print(len(answers))
