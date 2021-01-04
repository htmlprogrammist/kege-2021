# 22 задание
# Сколько существует чисел x, не превышающих 500, при вводе которых программа выведет 13
# x = int(input())
# S = 0
# while x > 0:
#     if x % 5 > 0:
#         S = S + (x % 5)
#     else:
#         S = S * (x % 5)
#     x = x // 5
# print(S)  # 13


answer = 13
x = 0
list_x = []
while x <= 500:
    S = 0
    number = x
    while number > 0:
        if number % 5 > 0:
            S = S + (number % 5)
        else:
            S = S * (number % 5)
        number = number // 5
    if S == answer:
        list_x.append(x)
    x += 1
# print(S)  # 13
print(list_x)
print(len(list_x))
