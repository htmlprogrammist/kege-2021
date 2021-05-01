"""
Задание 22 (№834).
Ниже на четырёх языках программирования записан алгоритм.
Получив на вход число x, этот алгоритм печатает два числа: L и M.
Укажите наибольшее число x, не содержащее нулей,
при вводе которого алгоритм печатает сначала 14, а потом 3.
"""

# x = int(input())
# L, M, R = 0, 0, 0
# while x > 0:
#     R = R * 10 + x % 10
#     x //= 10
#     if x <= R:
#         M += 1
#     else:
#         L += x % 10
# print(L)
# print(M)

answers = []
number = 0
answer_L = 14
answer_M = 3
while number < 10000000:
    x = number
    zero = False  # По умолчанию нулей нет
    L, M, R = 0, 0, 0
    while x > 0:
        R = R * 10 + x % 10
        x //= 10
        if x <= R:
            M += 1
        else:
            L += x % 10
    if answer_L == L and answer_M == M:
        check_number = number
        while check_number > 0:  # Расчехляем число по цифрам и смотрим на наличие 0
            last_digit = check_number % 10
            if last_digit == 0:
                zero = True  # Ноль есть
            check_number //= 10
        if not zero:  # Если нет нулей, то добавь к ответам
            answers.append(number)
    number += 1

print(answers)
print(max(answers))
