"""
Задание 23 (№278).
У исполнителя Калькулятор две команды, которым присвоены номера:
1. прибавь 1
2. увеличь число десятков на 1
Например: при помощи команды 2 число 23 преобразуется в 33. 
Если перед выполнением команды 2 вторая с конца цифра равна 9, она не изменяется.
Сколько есть программ, которые число 10 преобразуют в число 33? 

25
"""

k = [0] * (33 + 1)
k[10] = 1


def a_cannon_at_sparrows(number):
    if number // 10 == 9:  # по условию
        pass  # Но, учитывая диапозон с 10 по 33, это вообще не нужно
    else:
        dozen_in = number // 10
        dozen_out = dozen_in + 1
    return dozen_out * 10 + number % 10


for n in range(10, 33 + 1):
    if n + 1 <= 33:
        k[n + 1] += k[n]
    intermediate_result = a_cannon_at_sparrows(n)
    if intermediate_result <= 33:
        k[intermediate_result] += k[n]
    # if n + 10 <= 33:
    #     k[n + 10] += k[n]

print(k[33])
